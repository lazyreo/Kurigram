from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("APP_BOT_TOKEN")
API_ID = os.getenv("APP_API_ID")
API_HASH = os.getenv("APP_API_HASH")
DROPLINK_API_KEY = os.getenv("DROPLINK_API_KEY")
MY_CHANNEL_ID = os.getenv("MY_CHANNEL_ID")