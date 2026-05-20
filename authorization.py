
from pyromod import Client

from config import API_HASH, API_ID, BOT_TOKEN


bot = Client(
    "my_bot",
    api_id=API_ID,
    bot_token=BOT_TOKEN,
    api_hash=API_HASH

)
