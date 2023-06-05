from telethon import TelegramClient
import logging
import time 


openai_key = "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"
api_id = "1125689"

api_hash = "4772d1792ed194020a8fb06a91ffb8fa"

bot_token = "6161166370:AAHzWDo1ozz_dTGEhtPdDD3HNU6SrklNBtI"

bot = TelegramClient("coder", api_id, api_hash
   ).start(bot_token = bot_token)