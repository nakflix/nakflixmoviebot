import random
import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import BOT_START_TIME, ADMINS
from utils import humanbytes  

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝖡𝗎𝖽𝖽𝗒 𝖨𝖺𝗆 𝖠𝗅𝗂𝗏𝖾 :) 𝖧𝗂𝗍 /start \n\n𝖧𝗂𝗍 /help 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉 ;)\n\n\n𝖧𝗂𝗍 /ping 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖯𝗂𝗇𝗀 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("𝖧𝗂𝗍 /movie 𝖥𝗈𝗋 𝖬𝗈𝗏𝗂𝖾 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n\n𝖧𝗂𝗍 /series 𝖥𝗈𝗋 𝖲𝖾𝗋𝗂𝖾𝗌 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n\n\n𝖧𝗂𝗍 /tutorial 𝖥𝗈𝗋 𝖯𝗋𝗈𝗉𝖾𝗋 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅 𝖵𝗂𝖽𝖾𝗈𝗌 🤗")


@Client.on_message(filters.command("movie", CMD))
async def movie(_, message):
    await message.reply_text("⚠️❗️ 𝗠𝗼𝘃𝗶𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁 ❗️⚠️\n\n📝 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾, 𝖸𝖾𝖺𝗋,(𝖨𝖿 𝗒𝗈𝗎 𝖪𝗇𝗈𝗐) 𝖶𝗂𝗍𝗁 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 📚\n\n🗣 𝖨𝖿 𝖨𝗍 𝗂𝗌 𝖺 𝖥𝗂𝗅𝗆 𝖲𝖾𝗋𝗂𝖾𝗌. 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖮𝗇𝖾 𝖡𝗒 𝖮𝗇𝖾 𝖶𝗂𝗍𝗁 𝖯𝗋𝗈𝗉𝖾𝗋 𝖭𝖺𝗆𝖾 🧠\n\n🖇𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\n\n• Robin Hood ✅\n• Robin Hood 2010✅\n• Kurup 2021 Kan✅ \n• Harry Potter and the Philosophers Stone✅\n• Harry Potter and the Prisoner of Azkaban✅\n\n🥱 𝖥𝗈𝗋 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖠𝗎𝖽𝗂𝗈𝗌 - 𝖪𝖺𝗇 𝖿𝗈𝗋 𝖪𝖺𝗇𝗇𝖺𝖽𝖺, 𝖬𝖺𝗅 - 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆, 𝖳𝖺𝗆 - 𝖳𝖺𝗆𝗂𝗅\n\n🔎 𝖴𝗌𝖾 𝖥𝗂𝗋𝗌𝗍 3 𝖫𝖾𝗍𝗍𝖾𝗋𝗌 𝖮𝖿 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖥𝗈𝗋 𝖠𝗎𝖽𝗂𝗈𝗌 [𝖪𝖺𝗇 𝖳𝖺𝗆 𝖳𝖾𝗅 𝖬𝖺𝗅 𝖧𝗂𝗇 𝖲𝗉𝖺 𝖤𝗇𝗀 𝖪𝗈𝗋 𝖾𝗍𝖼...]\n\n❌ [𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝘄𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗗𝘂𝗯𝗯𝗲𝗱/𝗠𝗼𝘃𝗶𝗲𝘀/𝗦𝗲𝗻𝗱/𝗛𝗗 , . : - 𝗲𝘁𝗰] ❌")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⚠️❗️ 𝗦𝗲𝗿𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁 ❗️⚠️\n\n🗣 𝖲𝖾𝗋𝗂𝖾𝗌 𝖭𝖺𝗆𝖾,𝖲𝖾𝖺𝗌𝗈𝗇 (𝖶𝗁𝗂𝖼𝗁 𝖲𝖾𝖺𝗌𝗈𝗇 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍) 🧠\n\n🖇𝐄𝐱𝐚𝐦𝐩𝐥𝐞: \n\n• Game Of Thrones S03𝖤02 720𝗉✅\n• Sex Education S02 720p✅ \n• Breaking Bad S01E05✅ \n• Prison Break 1080p✅ \n• Witcher S02✅\n\n🥱 𝖥𝗈𝗋 𝖲𝖾𝖺𝗌𝗈𝗇 𝖬𝖾𝗇𝗍𝗂𝗈𝗇 𝖠𝗌 𝖲01 𝖥𝗈𝗋 𝖲𝖾𝖺𝗌𝗈𝗇 1, 𝖲02 𝖥𝗈𝗋 𝖲𝖾𝖺𝗌𝗈𝗇 2 𝖾𝗍𝖼 [𝖲03,𝖲04 ,𝖲06,𝖲10,𝖲17] 𝖦𝗈𝖾𝗌 𝖫𝗂𝗄𝖾 𝖳𝗁𝖺𝗍\n\n🔎 𝖥𝗈𝗋 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 𝖬𝖾𝗇𝗍𝗂𝗈𝗇 𝖠𝗌 𝖤𝗉01 𝖥𝗈𝗋 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 1, 𝖤𝗉02 𝖥𝗈𝗋 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 2 𝖾𝗍𝖼 [𝖤𝗉03,𝖤𝗉07,𝖤𝗉17,𝖤𝗉21] 𝖦𝗈'𝗌 𝖫𝗂𝗄𝖾 𝖳𝗁𝖺𝗍 \n\n❌ [𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝘄𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗦𝗲𝗮𝘀𝗼𝗻/𝗘𝗽𝗶𝘀𝗼𝗱𝗲/𝗦𝗲𝗿𝗶𝗲𝘀 , . : - 𝗲𝘁𝗰] ❌")

@Client.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    await message.reply_text("𝖢𝗁𝖾𝖼𝗄𝗈𝗎𝗍 @NAKFLIXTVTUTORIALS 𝖥𝗈𝗋 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅𝗌 😎")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")

@Client.on_message(filters.command("status"))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b>⚙️ 𝖡𝗈𝗍 𝖲𝗍𝖺𝗍𝗎𝗌</b>

🕔 𝖴𝗉𝗍𝗂𝗆𝖾: <code>{currentTime}</code>
🛠 𝖢𝖯𝖴 𝖴𝗌𝖺𝗀𝖾: <code>{cpu_usage}%</code>
🗜 𝖱𝖠𝖬 𝖴𝗌𝖺𝗀𝖾: <code>{ram_usage}%</code>
🗂 𝖳𝗈𝗍𝖺𝗅 𝖣𝗂𝗌𝗄 𝖲𝗉𝖺𝖼𝖾: <code>{total}</code>
🗳 𝖴𝗌𝖾𝖽 𝖲𝗉𝖺𝖼𝖾: <code>{used} ({disk_usage}%)</code>
📝 𝖥𝗋𝖾𝖾 𝖲𝗉𝖺𝖼𝖾: <code>{free}</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__𝖯𝗋𝗈𝖼𝖾𝗌𝗌𝗂𝗇𝗀...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**𝖡𝗈𝗍 𝖨𝗌 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀...🪄**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 ! 𝖱𝖾𝖺𝖽𝗒 𝖳𝗈 𝖬𝗈𝗏𝖾 𝖮𝗇 💯**")
    os.execl(sys.executable, sys.executable, *sys.argv)
