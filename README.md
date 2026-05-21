# Kurigram - Telegram URL Shortener Bot

A Telegram bot built with Pyrogram and Droplink that shortens HTTPS URLs while enforcing channel membership.

## Features

- ✅ Channel membership enforcement before URL shortening
- ✅ Shortens messages starting with `https`
- ✅ Replies with a prompt for non-URL messages
- ✅ Sends an inline **Open** button with the shortened link
- ✅ Handles Droplink API request errors and prints details to console

## Project Structure

```
├── main.py              # Main bot logic and message handlers
├── authorization.py     # Pyrogram client initialization for the bot
├── config.py            # Loads environment variables from .env
├── api_client.py        # Sends requests to Droplink and parses JSON responses
├── pyproject.toml       # Project metadata and dependencies
├── requirements.txt     # Placeholder file
└── README.md            # Project documentation
```

## Dependencies

Dependencies are declared in `pyproject.toml`.

- `dotenv`
- `pyrogram`
- `pyromod`
- `requests`
- `tgcrypto`

> `requirements.txt` is currently a placeholder. Install dependencies with `pip` or `poetry install`.

## Setup Instructions

### 1. Prerequisites

- Python 3.11 or higher
- Telegram Bot Token from [@BotFather](https://t.me/botfather)
- Telegram API credentials (`API_ID` and `API_HASH`) from [my.telegram.org](https://my.telegram.org)
- Droplink API Key from [droplink.co](https://droplink.co)

### 2. Installation

Install the required packages:

```bash
python -m pip install -U pip
python -m pip install pyrogram pyromod requests dotenv tgcrypto
```

Or use Poetry:

```bash
poetry install
```

### 3. Environment Configuration

Create a `.env` file in the project root with:

```env
APP_BOT_TOKEN=your_bot_token_here
APP_API_ID=your_api_id_here
APP_API_HASH=your_api_hash_here
DROPLINK_API_KEY=your_droplink_api_key_here
MY_CHANNEL_ID=your_channel_id_or_username_here
```

`MY_CHANNEL_ID` is used for the Telegram channel membership check.

## How It Works

### `authorization.py`

Initializes the Pyrogram client:

- `my_bot` session name
- `api_id`, `api_hash`, and `bot_token` from `config.py`

### `config.py`

Loads the environment variables from `.env`:

- `BOT_TOKEN` from `APP_BOT_TOKEN`
- `API_ID` from `APP_API_ID`
- `API_HASH` from `APP_API_HASH`
- `DROPLINK_API_KEY`
- `MY_CHANNEL_ID`

### `api_client.py`

Requests the Droplink API with:

- `api`: the Droplink API key
- `url`: the original URL to shorten

It prints the HTTP status and response body, and handles common request errors.

### `main.py`

1. **Channel membership enforcement** (`group=1`)
   - Calls `get_chat_member` on `MY_CHANNEL_ID`
   - If the user is not a channel member, replies with a join button and stops further processing
   - If the user is a member, allows the message to continue to later handlers

2. **Non-HTTPS text handling** (`group=2`, `~pyrogram.filters.regex(r"^https")`)
   - Replies with a friendly prompt asking the user to send a lengthy URL

3. **HTTPS URL shortening** (`group=2`, `pyrogram.filters.regex(r"^https")`)
   - Sends the URL to Droplink
   - Extracts `shortenedUrl` from the JSON response
   - Replies with the shortened link and an inline `Open` button

> Note: The join button URL is currently hard-coded to `https://t.me/practicekurigram` in `main.py`.

## Usage

Run the bot:

```bash
python main.py
```

Then message the bot on Telegram:

- Non-URL messages will receive a prompt to send a URL
- Messages starting with `https` will be shortened
- The bot replies with a shortened URL and an inline button

## Notes

- `requirements.txt` is not populated; use the `pyproject.toml` dependencies instead.
- `register_user.py` is not present in this repository and is not part of the current implementation.

## License

This project is for educational purposes.
