# Kurigram - Telegram URL Shortener Bot

A Telegram bot that shortens lengthy URLs using the Droplink API. This bot requires users to be members of a specific channel before they can use its services.

## Features

- ✅ **Channel Membership Check**: Verifies that users are members of a designated Telegram channel before allowing access
- ✅ **URL Shortening**: Converts lengthy URLs into shortened versions using the Droplink API
- ✅ **Interactive UI**: Provides an inline button to directly open shortened URLs
- ✅ **User-Friendly Messages**: Guides users with clear instructions and friendly responses

## Project Structure

```
├── tiny_url.py          # Main bot handler with message processing logic
├── authorization.py     # Telegram bot client initialization
├── config.py            # Environment configuration loader
├── api_client.py        # API client for making requests to Droplink
├── pyproject.toml       # Project metadata and dependencies
├── requirements.txt     # Optional dependency lock / install list
└── README.md            # This file
```

## Dependencies

This project uses the dependencies declared in `pyproject.toml` and also includes a `requirements.txt` lock-style file for installing the same packages.

- `pyrogram`: Telegram bot framework
- `pyromod`: Extensions for Pyrogram
- `requests`: HTTP library for API requests
- `python-dotenv`: Environment variable management
- `tgcrypto`: Encryption support for Telegram
- `qrcode`: QR code generation
- `reloadium`: Development reload utility

## Setup Instructions

### 1. Prerequisites

- Python 3.11 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Telegram API credentials (`API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org))
- Droplink API Key (from [droplink.co](https://droplink.co))

### 2. Installation

Install dependencies using one of the following options.

Option A: Install from `requirements.txt`:

```bash
python -m pip install -U pip
python -m pip install -r requirements.txt
```

Option B: Install the required packages directly from `pyproject.toml`:

```bash
python -m pip install -U pip
python -m pip install pyrogram pyromod requests python-dotenv tgcrypto qrcode reloadium
```

Option C: If you use Poetry:

```bash
poetry install
```

### 3. Environment Configuration

Create a `.env` file in the project root with the following variables:

```env
APP_BOT_TOKEN=your_bot_token_here
APP_API_ID=your_api_id_here
APP_API_HASH=your_api_hash_here
DROPLINK_API_KEY=your_droplink_api_key_here
MY_CHANNEL_ID=your_channel_id_here
```

`MY_CHANNEL_ID` should be the numeric ID of the channel that users must join.

## How It Works

### Message Filtering

The bot uses Pyrogram's filter system with priority groups:

1. **Group 1 - Channel Membership Check**:
   - Checks if the user is a member of `MY_CHANNEL_ID`
   - If user is not a member, sends a "Join Channel" prompt
   - If user is a member, continues to next group

2. **Group 2 - URL Processing**:
   - **Non-URL Messages**: Sends a friendly greeting and instructions
   - **URL Messages**: Accepts URLs starting with `https`, shortens them via Droplink API, and returns the shortened URL with an "Open" button

### API Integration

The bot communicates with the Droplink API to shorten URLs:

- **Endpoint**: `https://droplink.co/api`
- **Parameters**: API key and target URL
- **Response**: Returns the shortened URL as JSON

## Usage

1. Start the bot:
   ```bash
   python tiny_url.py
   ```

2. On Telegram:
   - Send `/start` to the bot
   - If not a channel member, click the "Join" button
   - Send any lengthy URL (starting with `https`) to get it shortened
   - Click the "Open" button to visit the shortened URL

## Error Handling

The API client handles various HTTP errors gracefully:

- HTTP errors
- Connection errors
- Request timeouts
- Redirect errors
- JSON decode errors

All errors are logged to the console for debugging.

## License

This project is for educational purposes.
