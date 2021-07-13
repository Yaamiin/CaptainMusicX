from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
     
       await message.reply_text(
        f"""**ᴘʀᴏꜰᴇꜱꜱɪᴏɴᴀʟ ᴜᴘᴅᴀᴛᴇᴅ ᴍᴜꜱɪᴄ ʙᴏᴛ🌹

ᴛʜɪꜱ ʙᴏᴛ ʀᴜɴ ᴏɴ ꜱᴀɴᴋɪ ᴘʀɪᴠᴀᴛᴇ ꜱᴇʀᴠᴇʀ. ᴅᴇᴘʟᴏʏ ᴏɴ ᴀᴅᴠᴀɴᴄᴇ ᴘʀɪᴠᴀᴛᴇ ʀᴇᴘᴏ[⭐| ᴛᴇᴛᴏʀɪᴀʟ |⭐](https://youtu.be/zePiU0tGN-k).

ᴀᴅᴅ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 ᴄᴏᴍᴍᴀɴᴅ 🌸", url="https://t.me/SankiAutobot/12")
                  ],[
                    InlineKeyboardButton(
                        "💬 ꜱᴀɴᴋɪ ᴘᴜʙʟɪᴄ", url="https://t.me/BrandSanki"
                    ),
                    InlineKeyboardButton(
                        "🌀 ᴇꜱᴘᴏʀᴛ ᴄʟᴀɴ", url="https://t.me/EsportCheater"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/SankiServerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ꜱᴀɴᴋɪ ꜱᴇʀᴠᴇʀ ᴏɴʟɪɴᴇ ɴᴏᴡ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌀 ᴄʜᴀɴɴᴇʟ", url="https://t.me/SankiAutobot")
                ]
            ]
        )
   )


