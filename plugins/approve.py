from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserIsBlocked, PeerIdInvalid


@Client.on_chat_join_request()
async def accept_request(client, r):

    rm = InlineKeyboardMarkup([[
        InlineKeyboardButton("❤sᴇʀɪᴇs🎥", url="https://t.me/NAKFLIXTV"),
        InlineKeyboardButton("⚡ᴍᴏᴠɪᴇs⚡", url="https://t.me/NAKFLIXPLUS")
    ]])
    
    try:
        await client.send_photo(
            r.from_user.id,
            'https://telegra.ph/file/9e8ff574c512c53cd6bf2.jpg',
            f"**ʜᴇʟʟᴏ {r.from_user.mention} 👻, ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {r.chat.title}\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ...!!!**",
            reply_markup=rm)

    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid:
        print("Err")
    except Exception as e:
        print(f"#Error\n{str(e)}")

    await r.approve()
