from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**ᴘʀᴏꜰꜱꜱɪᴏɴᴀʟ ᴅᴀᴛᴀʙᴀꜱᴇ ʜᴏꜱᴛɪɴɢ 

ᴇꜱᴘᴏʀᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ ʜᴏꜱᴛ ᴏɴ ᴘʀɪᴠᴀᴛᴇ ꜱᴇʀᴠᴇʀ. ᴜꜱɪɴɢ ʜɪɢʜ ᴄᴏɴꜰɪɢ ɴᴏ ʟᴀɢ ꜰᴜʟʟ ᴍᴀꜱᴛɪ🎶[🌹| ᴇꜱᴘᴏʀᴛ ᴄʟᴀɴ |🌹](https://t.me/EsportCheater).

ᴛʜɪꜱ ʙᴏᴛ ʜᴏꜱᴛ ᴏɴ ꜰɪʀᴇʙᴀꜱᴇ ꜱᴇʀᴠᴇʀ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹ᴇꜱᴘᴏʀᴛ ᴄʟᴀɴ ", url="https://t.me/EsportCheater")
                  ],[
                    InlineKeyboardButton(
                        "⭐ ꜱᴀɴᴋɪ ᴘᴜʙʟɪᴄ", url="https://t.me/BrandSanki"
                    ),
                    InlineKeyboardButton(
                        "🔊 ᴏᴡɴᴇʀ", url="https://t.me/its_Hexor"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/EsportMusicRobot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ɢʀᴏᴜᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ᴏɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 ᴏᴡɴᴇʀ", url="https://t.me/Its_Hexor")
                ]
            ]
        )
   )





