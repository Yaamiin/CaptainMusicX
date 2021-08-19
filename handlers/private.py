from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
❰ꜱᴍᴏᴋᴇʀ✘ʜᴇxᴏʀ❱ ꜱᴜᴘᴇʀ ꜰᴀꜱᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴄ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴇʟ ʜɪɢʜ Qᴜᴇʟɪᴛʏ ᴍᴜꜱɪᴄ [ɢʀᴏᴜᴘ](https://t.me/EsportCheater).
Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰Oᴡɴᴇʀ❱", url="https://t.me/Its_Hexor")
                  ],[
                    InlineKeyboardButton(
                        "❰Sᴜᴩᴩᴏʀᴛ❱", url="https://t.me/EsportCheater"
                    ),
                    InlineKeyboardButton(
                        "❰ɢʀᴏᴜᴘ❱", url="https://t.me/EsportCheater"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰ᴀᴅᴅ ᴍᴇ ɪɴ ᴜʀ ɢʀᴏᴜᴘ❱", url="https://t.me/EsportPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aᴍ Oɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/EsportCheater")
                ]
            ]
        )
   )
