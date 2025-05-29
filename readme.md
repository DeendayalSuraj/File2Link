![GitHub contributors](https://img.shields.io/github/contributors/biisal/biisal-file-stream-pro?style=flat&color=green)
![GitHub repo size](https://img.shields.io/github/repo-size/biisal/biisal-file-stream-pro?color=green)
![GitHub](https://img.shields.io/github/license/biisal/biisal-file-stream-pro?color=green)

### Demo Bot

Here is our Demo bot -

[![Click Here](https://img.shields.io/badge/Demo%20Bot-Click%20Here-blue?style=flat&logo=telegram&labelColor=white&link=https://t.me/Bisal_Files_Talk)](https://t.me/Bisal_File2Link_Bot)

### Need Deployment Support?

If you encounter any issues deploying the bot, feel free to seek assistance in our support group:

[![Join Support Group](https://img.shields.io/badge/Join%20Support%20Group-Click%20Here-blue?style=flat&logo=telegram&labelColor=white&link=https://t.me/Bisal_Files_Talk)](https://t.me/Bisal_Files_Talk)



<h1 align="center"></h1>
<p align="center"> 
  <img src="https://wallpapercave.com/wp/wp12026024.jpg" alt="Cover Image" width="650">
  </a>
  
 <p align="center">
    A Telegram bot to turn all media and documents files to instant direct download and stream link .
    <br />
   </strong></a>
    <br />
    <a href="https://github.com/biisal/biisal-file-stream-pro/issues">Report a Bug</a>
    |
    <a href="https://github.com/biisal/biisal-file-stream-pro/issues">Request Feature</a>
  </p>


<hr>

## Project Discontinuation Notice and Disclaimer

**Please Note**:

This project has been discontinued and is no longer actively maintained or updated. As a result, it may contain outdated dependencies or potential security vulnerabilities.

**Disclaimer:**

This code is provided as-is, for educational purposes only, with no support or warranty. The developer is not liable for any legal consequences, damages, or issues that may arise from its use.

By using this code, you accept these terms and conditions, agreeing that all risks and responsibilities lie with you, the end user. Ensure the code's suitability for your needs before proceeding.

Feel free to use the existing code for educational or reference purposes, but be aware that it may not be suitable for production use without significant updates and improvements.

Thank you for your interest in this project, and we appreciate your understanding regarding its discontinuation.

<hr>

## 🍁 About This Bot :

![streamingfilestreambot-professional-live_1](https://t3.ftcdn.net/jpg/05/97/92/78/240_F_597927853_iZIpn7Blgg3TPd1XEKgF1KhLRuqNxhiU.jpg)

</p>
<p align='center'>
    This bot will give you streamable download links for Telegram files without the need of waiting till the download completes.
</p>


<br>
<details>
  <summary><b>Features:</b></summary>
  
<p>

🚀Features<p>
💥Superfast⚡️ download and stream links.<br>
💥No ads in generated links.<br>
💥Superfast interface.<br>
💥Along with the links you also get file information like name,size ,etc.<br>
💥Updates channel Support.<br>
💥Mongodb database support for broadcasting.<br>
💥Password Protection.<br>
💥User DC Check.<br>
💥Custom Domain support. <br>
💥All unwanted code removed. <br>
💥A lot more tired of writing check out by deploying it. 
</details>
  <details>
      <summary><b>Deploy to Heroku<b></summary>
      Click the button below to deploy the bot on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/biisal/biisal-file-stream-pro)

  </details>
  <details>
  <summary><b>Deploy on Windows or other plataform<b></summary>
  
  You should make sure you have Python 3.6+ installed on your PC, then clone this repo and run the following commands in a terminal:

```py
git clone https://github.com/biisal/biisal-file-stream-pro
cd filestreambot-pro
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m biisal
```



and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

 </details>
</details>
<details>
  <summary><b>Vars and Details :</b></summary>

Go to a file named `Vars.py` in the `biisal` Named File and add all the variables there.
An example of `Vars.py` file:

```py
API_ID=12345
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=Your_Bot_Token
BIN_CHANNEL=-100
PORT=8080
FQDN=your_server_ip
OWNER_ID=your_user_id
DATABASE_URL=mongodb_uri
```
`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.
  
`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Create a new channel (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.
  
`OWNER_USERNAME` : U should be knowing it afterall it's your username dont remember it? just go to settings!

`OWNER_ID` : Your Telegram User ID

`DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can click on logo below!

[![mongo](https://telegra.ph/file/fd68906852c71fdd68bef.jpg)](https://www.youtube.com/watch?v=HhHzCfrqsoE)

 Option Vars

`UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.

`BANNED_CHANNELS` : Put IDs of Banned Channels where bot will not work. You can add multiple IDs & separate with <kbd>Space</kbd>.

`SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.

`WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`

`PORT` : The port that you want your webapp to be listened to. Defaults to `8080`

`WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`

`NO_PORT` : If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.

`FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS` </details>

<details>
  <summary><b>How to Use :</b></summary>

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an Admin**
 
`/start` : To check if the bot is alive or not.

To get an instant stream link, just forward any media to the bot and boom, its 🚀🚀.
  
![image](https://i.postimg.cc/7hbFzd7X/20231212-235124.jpg)


### Channel Support
Bot also Supported with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button. </details>

### Credits : 

- [Me](https://github.com/biisal)
- [Adarsh](https://github.com/adarsh-goel)
- Everyone In This Journey !


## API for WordPress Integration

This Python application provides an API endpoint to generate direct download/streamable links for files managed by the Telegram bot. This is intended for use by a WordPress plugin or any other service that needs to programmatically obtain these links.

### Endpoint Details

*   **URL:** `/api/v1/generate_link`
    *   The full URL will be `YOUR_PYTHON_SERVICE_BASE_URL/api/v1/generate_link` (e.g., `https://your-app-name.herokuapp.com/api/v1/generate_link` or `http://your_server_ip:PORT/api/v1/generate_link`).
*   **HTTP Method:** `POST`
*   **Content-Type:** `application/json`

### Request Payload

The request must be a JSON object with the following fields:

```json
{
    "api_key": "YOUR_SECRET_API_KEY",
    "chat_id": CHAT_ID_OF_THE_MESSAGE_WITH_FILE,
    "message_id": MESSAGE_ID_OF_THE_FILE
}
```

*   `api_key` (string, required): Your secret API key. This must match the `WP_PLUGIN_API_KEY` configured in the Python service's environment variables.
*   `chat_id` (integer or string, required): The Telegram Chat ID where the message containing the file is located. For channels, this is usually a negative number (e.g., -1001234567890). For private chats, it's the user ID.
*   `message_id` (integer, required): The ID of the Telegram message that contains the file.

### Authentication

Authentication is done via the `api_key` sent in the JSON payload.
If the API key is missing, invalid, or the `WP_PLUGIN_API_KEY` is not configured on the server, an HTTP 401 Unauthorized error will be returned.

### Success Response (200 OK)

If the request is successful, the server will respond with a JSON object containing the download link:

```json
{
    "download_link": "GENERATED_DOWNLOAD_STREAM_LINK"
}
```
Example:
```json
{
    "download_link": "https://your-python-service.com/ab123fg67890"
}
```
This link can then be used to directly download or stream the file.

### Error Responses

*   **400 Bad Request:**
    *   If the JSON payload is malformed or missing required fields.
    ```json
    {
        "error": "Invalid JSON payload"
    }
    ```
    *   If `chat_id` or `message_id` are not valid integers.
    ```json
    {
        "error": "chat_id and message_id must be integers"
    }
    ```
*   **401 Unauthorized:**
    *   If the `api_key` is invalid or missing.
    ```json
    {
        "error": "Unauthorized"
    }
    ```
*   **404 Not Found:**
    *   If the specified message is not found in the given chat, or if the message does not contain any media/file.
    ```json
    {
        "error": "File not found or message has no media"
    }
    ```
*   **415 Unsupported Media Type:**
    *   If the `Content-Type` header is not `application/json`.
    ```json
    {
        "error": "Unsupported Media Type"
    }
    ```
*   **500 Internal Server Error:**
    *   If there's an unexpected error on the server while trying to fetch file details from Telegram or during other operations.
    ```json
    {
        "error": "Error fetching file details from Telegram" 
    }
    ```
    (The error message might vary slightly)
*   **503 Service Unavailable:**
    *   If Telegram services are temporarily unavailable or the bot is under heavy load.
    ```json
    {
        "error": "Service temporarily unavailable, please try again later."
    }
    ```

### Example: Calling the API from PHP (WordPress)

Here's a basic example of how you might call this API endpoint using PHP, which can be adapted for a WordPress plugin:

```php
<?php

function get_telegram_file_download_link($api_url, $api_key, $chat_id, $message_id) {
    $payload = json_encode([
        'api_key' => $api_key,
        'chat_id' => $chat_id,
        'message_id' => (int)$message_id // Ensure message_id is an integer
    ]);

    $args = [
        'body'        => $payload,
        'headers'     => [
            'Content-Type' => 'application/json',
        ],
        'method'      => 'POST',
        'data_format' => 'body',
        'timeout'     => 15, // Optional: set a timeout
    ];

    // In WordPress, you would use wp_remote_post()
    // $response = wp_remote_post($api_url, $args);

    // For generic PHP, you might use cURL:
    $ch = curl_init($api_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Content-Length: ' . strlen($payload)
    ]);

    $response_body = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    // --- Processing the response (common for both wp_remote_post and cURL) ---

    // Example for wp_remote_post:
    // if (is_wp_error($response)) {
    //     return ['error' => 'Request failed: ' . $response->get_error_message()];
    // }
    // $http_code = wp_remote_retrieve_response_code($response);
    // $response_body = wp_remote_retrieve_body($response);

    if ($http_code === 200) {
        $data = json_decode($response_body, true);
        return $data; // Should contain ['download_link' => '...']
    } elseif ($response_body) {
        $error_data = json_decode($response_body, true);
        return ['error' => isset($error_data['error']) ? $error_data['error'] : 'Unknown error', 'status_code' => $http_code];
    } else {
        return ['error' => 'API request failed with no response body', 'status_code' => $http_code];
    }
}

// --- How to use it ---
// $python_service_api_url = 'YOUR_PYTHON_SERVICE_BASE_URL/api/v1/generate_link';
// $your_api_key = 'YOUR_SECRET_API_KEY_CONFIGURED_IN_PYTHON_SERVICE';
// $target_chat_id = -1001234567890; // Example channel ID
// $target_message_id = 123;       // Example message ID

// $result = get_telegram_file_download_link(
//     $python_service_api_url,
//     $your_api_key,
//     $target_chat_id,
//     $target_message_id
// );

// if (isset($result['download_link'])) {
//     echo "Download Link: " . $result['download_link'];
// } elseif (isset($result['error'])) {
//     echo "Error: " . $result['error'] . (isset($result['status_code']) ? " (Status: " . $result['status_code'] . ")" : "");
// }

?>
```

Make sure to replace `YOUR_PYTHON_SERVICE_BASE_URL` and `YOUR_SECRET_API_KEY` with your actual service URL and API key. The `chat_id` and `message_id` would typically come from your WordPress plugin's logic or settings.
