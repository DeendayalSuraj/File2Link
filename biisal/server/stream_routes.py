# Taken from megadlbot_oss <https://github.com/eyaadh/megadlbot_oss/blob/master/mega/webserver/routes.py>
# Thanks to Eyaadh <https://github.com/eyaadh>
# Thanks to adarsh-goel
# (c) @biisal
import re
import time
import math
import logging
import secrets
import mimetypes
import json # Added for JSON parsing
from aiohttp import web
from aiohttp.http_exceptions import BadStatusLine
from pyrogram.errors import MessageIdInvalid # Added for specific exception handling
from biisal.bot import multi_clients, work_loads, StreamBot
from biisal.server.exceptions import FIleNotFound, InvalidHash
from biisal import StartTime, __version__
from ..utils.time_format import get_readable_time
from ..utils.custom_dl import ByteStreamer
from biisal.utils.render_template import render_page
from biisal.vars import Var

# Define logger for this module
logger = logging.getLogger(__name__)

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(_):
    return web.json_response(
        {
            "server_status": "running",
            "uptime": get_readable_time(time.time() - StartTime),
            "telegram_bot": "@" + StreamBot.username,
            "connected_bots": len(multi_clients),
            "loads": dict(
                ("bot" + str(c + 1), l)
                for c, (_, l) in enumerate(
                    sorted(work_loads.items(), key=lambda x: x[1], reverse=True)
                )
            ),
            "version": __version__,
        }
    )


@routes.post("/api/v1/generate_link")
async def generate_link_handler(request: web.Request):
    try:
        if request.content_type != 'application/json':
            logger.warning(f"Invalid content type received: {request.content_type}")
            return web.json_response({"error": "Invalid content type, expected application/json"}, status=415)

        try:
            data = await request.json()
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON body received: {e}")
            return web.json_response({"error": "Invalid JSON body"}, status=400)

        api_key = data.get("api_key")
        chat_id_str = data.get("chat_id")
        message_id_str = data.get("message_id")

        if not all([api_key, chat_id_str, message_id_str]):
            logger.warning("Missing one or more required fields in API request.")
            return web.json_response({"error": "Missing required fields: api_key, chat_id, message_id"}, status=400)

        if api_key != Var.WP_PLUGIN_API_KEY:
            logger.warning(f"Unauthorized API access attempt with key: {api_key[:5]}...") # Log only a portion of the key
            return web.json_response({"error": "Unauthorized"}, status=401)

        try:
            chat_id = int(chat_id_str)
            message_id = int(message_id_str)
        except ValueError:
            logger.warning(f"Invalid chat_id or message_id format: chat_id='{chat_id_str}', message_id='{message_id_str}'")
            return web.json_response({"error": "Invalid chat_id or message_id format, must be integers"}, status=400)

        client_to_use = StreamBot
        if Var.MULTI_CLIENT:
            if not work_loads:
                logger.error("No clients available in work_loads for MULTI_CLIENT mode.")
                return web.json_response({"error": "Server configuration error, no clients available"}, status=503) 
            client_index = min(work_loads, key=work_loads.get)
            client_to_use = multi_clients[client_index]
            logger.info(f"Using client {client_index} for API request (chat_id: {chat_id}, msg_id: {message_id}).")
        else:
            logger.info(f"Using default client StreamBot for API request (chat_id: {chat_id}, msg_id: {message_id}).")
        
        message = None
        try:
            fetched_item = await client_to_use.get_messages(chat_id=chat_id, message_ids=message_id)
            if isinstance(fetched_item, list):
                message = fetched_item[0] if fetched_item else None
            else:
                message = fetched_item
        except MessageIdInvalid:
            logger.warning(f"Message not found (MessageIdInvalid) for chat_id {chat_id}, message_id {message_id}")
            return web.json_response({"error": "Message not found or invalid ID"}, status=404)
        except Exception as e:
            logger.error(f"Error fetching message for chat_id {chat_id}, message_id {message_id}: {type(e).__name__} - {e}", exc_info=True)
            return web.json_response({"error": "Failed to retrieve message details from Telegram"}, status=500)

        if not message:
            logger.warning(f"Message object is None after fetching for chat_id {chat_id}, message_id {message_id}")
            return web.json_response({"error": "Message not found"}, status=404)

        media = message.media
        file_unique_id = None
        actual_message_id = message.id

        if media:
            if message.document and hasattr(message.document, 'file_unique_id'):
                file_unique_id = message.document.file_unique_id
            elif message.video and hasattr(message.video, 'file_unique_id'):
                file_unique_id = message.video.file_unique_id
            elif message.audio and hasattr(message.audio, 'file_unique_id'):
                file_unique_id = message.audio.file_unique_id
            elif message.photo and hasattr(message.photo, 'file_unique_id'):
                file_unique_id = message.photo.file_unique_id
        
        if not file_unique_id:
            logger.warning(f"Message (ID: {actual_message_id}) in chat {chat_id} does not contain usable media or file_unique_id.")
            return web.json_response({"error": "Message does not contain usable media or file_unique_id is missing"}, status=400)

        secure_hash = file_unique_id[:6]
        
        link = f"{Var.URL}{secure_hash}{actual_message_id}"
        if not Var.URL.endswith("/"):
            link = f"{Var.URL}/{secure_hash}{actual_message_id}"

        logger.info(f"Generated link for message {actual_message_id} in chat {chat_id}: {link}")
        return web.json_response({"download_link": link}, status=200)

    except Exception as e:
        logger.error(f"Unexpected error in generate_link_handler: {type(e).__name__} - {e}", exc_info=True)
        return web.json_response({"error": "An unexpected server error occurred"}, status=500)


@routes.get(r"/watch/{path:\S+}", allow_head=True)
async def stream_handler(request: web.Request):
    try:
        path = request.match_info["path"]
        match = re.search(r"^([a-zA-Z0-9_-]{6})(\d+)$", path)
        if match:
            secure_hash = match.group(1)
            id = int(match.group(2))
        else:
            id = int(re.search(r"(\d+)(?:\/\S+)?", path).group(1))
            secure_hash = request.rel_url.query.get("hash")
        return web.Response(text=await render_page(id, secure_hash), content_type='text/html')
    except InvalidHash as e:
        logger.warning(f"InvalidHash in /watch stream_handler: {e.message}") # Use module logger
        raise web.HTTPForbidden(text=e.message)
    except FIleNotFound as e:
        logger.warning(f"FIleNotFound in /watch stream_handler: {e.message}") # Use module logger
        raise web.HTTPNotFound(text=e.message)
    except (AttributeError, BadStatusLine, ConnectionResetError):
        logger.warning(f"Network related error in /watch stream_handler: {type(e).__name__}") # Use module logger
        pass
    except Exception as e:
        logger.critical(f"Critical error in /watch stream_handler: {e}", exc_info=True) # Use module logger
        raise web.HTTPInternalServerError(text=str(e))

@routes.get(r"/{path:\S+}", allow_head=True)
async def stream_handler(request: web.Request): # This is the second stream_handler, for the main path
    try:
        path = request.match_info["path"]
        match = re.search(r"^([a-zA-Z0-9_-]{6})(\d+)$", path)
        if match:
            secure_hash = match.group(1)
            id = int(match.group(2))
        else:
            id = int(re.search(r"(\d+)(?:\/\S+)?", path).group(1))
            secure_hash = request.rel_url.query.get("hash")
        return await media_streamer(request, id, secure_hash)
    except InvalidHash as e:
        logger.warning(f"InvalidHash in main stream_handler: {e.message}") # Use module logger
        raise web.HTTPForbidden(text=e.message)
    except FIleNotFound as e:
        logger.warning(f"FIleNotFound in main stream_handler: {e.message}") # Use module logger
        raise web.HTTPNotFound(text=e.message)
    except (AttributeError, BadStatusLine, ConnectionResetError):
        logger.warning(f"Network related error in main stream_handler (media_streamer path): {type(e).__name__}") # Use module logger
        pass
    except Exception as e:
        logger.critical(f"Critical error in main stream_handler: {e}", exc_info=True) # Use module logger
        raise web.HTTPInternalServerError(text=str(e))

class_cache = {}

async def media_streamer(request: web.Request, id: int, secure_hash: str):
    range_header = request.headers.get("Range", 0)
    
    index = min(work_loads, key=work_loads.get)
    faster_client = multi_clients[index]
    
    if Var.MULTI_CLIENT:
        logger.info(f"Client {index} is now serving {request.remote}") # Use module logger

    if faster_client in class_cache:
        tg_connect = class_cache[faster_client]
        logger.debug(f"Using cached ByteStreamer object for client {index}") # Use module logger
    else:
        logger.debug(f"Creating new ByteStreamer object for client {index}") # Use module logger
        tg_connect = ByteStreamer(faster_client)
        class_cache[faster_client] = tg_connect
    logger.debug("before calling get_file_properties") # Use module logger
    file_id = await tg_connect.get_file_properties(id)
    logger.debug("after calling get_file_properties") # Use module logger
    
    if file_id.unique_id[:6] != secure_hash:
        logger.debug(f"Invalid hash for message with ID {id}") # Use module logger
        raise InvalidHash
    
    file_size = file_id.file_size

    if range_header:
        from_bytes, until_bytes = range_header.replace("bytes=", "").split("-")
        from_bytes = int(from_bytes)
        until_bytes = int(until_bytes) if until_bytes else file_size - 1
    else:
        from_bytes = request.http_range.start or 0
        until_bytes = (request.http_range.stop or file_size) - 1

    if (until_bytes > file_size) or (from_bytes < 0) or (until_bytes < from_bytes):
        return web.Response(
            status=416,
            body="416: Range not satisfiable",
            headers={"Content-Range": f"bytes */{file_size}"},
        )

    chunk_size = 1024 * 1024
    until_bytes = min(until_bytes, file_size - 1)

    offset = from_bytes - (from_bytes % chunk_size)
    first_part_cut = from_bytes - offset
    last_part_cut = until_bytes % chunk_size + 1

    req_length = until_bytes - from_bytes + 1
    part_count = math.ceil(until_bytes / chunk_size) - math.floor(offset / chunk_size)
    body = tg_connect.yield__file(
        file_id, index, offset, first_part_cut, last_part_cut, part_count, chunk_size
    )

    mime_type = file_id.mime_type
    file_name = file_id.file_name
    disposition = "attachment"

    if mime_type:
        if not file_name:
            try:
                file_name = f"{secrets.token_hex(2)}.{mime_type.split('/')[1]}"
            except (IndexError, AttributeError):
                file_name = f"{secrets.token_hex(2)}.unknown"
    else:
        if file_name:
            mime_type = mimetypes.guess_type(file_id.file_name)
        else:
            mime_type = "application/octet-stream"
            file_name = f"{secrets.token_hex(2)}.unknown"

    return web.Response(
        status=206 if range_header else 200,
        body=body,
        headers={
            "Content-Type": f"{mime_type}",
            "Content-Range": f"bytes {from_bytes}-{until_bytes}/{file_size}",
            "Content-Length": str(req_length),
            "Content-Disposition": f'{disposition}; filename="{file_name}"',
            "Accept-Ranges": "bytes",
        },
    )
