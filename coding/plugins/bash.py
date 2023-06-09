import io 
import asyncio
from .. import bot
from telethon import events
import time

@bot.on(events.NewMessage(incoming=True, pattern="/bash ?(.*)"))
async def _bash(event):
    if event.fwd_from:
        return
    vtx = await event.reply("Processing")
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**Qᴜᴇʀʏ:**\n**Cᴏᴍᴍᴀɴᴅ:**\n`{cmd}` \n**Pɪᴅ**\n`{process.pid}`\n\n**Sᴛᴅᴇʀʀ:** \n`{e}`\n**Oᴜᴛᴘᴜᴛ:**\n{o}"
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )
            await event.delete()
    await vtx.edit(OUTPUT)
