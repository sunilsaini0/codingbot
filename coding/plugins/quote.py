from telethon.sync import TelegramClient, events
import requests
from .. import bot

@bot.on(events.NewMessage(pattern='/saying'))
async def share_saying(event):
    saying = fetch_saying()
    await event.reply(saying)

def fetch_saying():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        saying_data = response.json()
        content = saying_data['content']
        author = saying_data['author']
        return f"{content}\n\n- {author}"
    else:
        return 'Oops! Unable to fetch a saying at the moment.'