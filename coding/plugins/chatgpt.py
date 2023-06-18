from telethon import events
from .. import bot
import asyncio
import openai

openai.api_key = "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"
#openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern = "(?i)/ask"))
async def _gpt(event):
  #if event.sender_id ==int(5370621967):
  await event.reply("yes! you are My Developer you developed me very well")
  # else:
   # await event.reply("you are user: nice to meet you")
  
  await event.reply (event)
