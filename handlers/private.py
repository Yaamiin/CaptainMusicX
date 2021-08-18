from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
❰ꜱᴍᴏᴋᴇʀ✘ʜᴇxᴏʀ❱ ꜱᴜᴘᴇʀ ꜰᴀꜱᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴄ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴇʟ ʜɪɢʜ Qᴜᴇʟɪᴛʏ ᴍᴜꜱɪᴄ [ɢʀᴏᴜᴘ](https://t.me/SankiPublicEnjoy).
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
                        "❰ɢʀᴏᴜᴘ❱", url="https://t.me/SankiPublicEnjoy"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰ᴀᴅᴅ ᴍᴇ ɪɴ ᴜʀ ɢʀᴏᴜᴘ❱", url="https://t.me/EsportRoBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("song") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴛʜɪꜱ ʙᴏᴛ ʙʏ ❰ʜᴇxᴏʀ❱**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰Uᴩᴅᴀᴛᴇs❱", url="https://t.me/SankiPublicEnjoy")
                ]
            ]
        )
   )


@Client.on_message(filters.command("ban") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴀᴅᴅ ꜱᴀɴᴋɪ ʀᴏʙᴏᴛ ꜰᴏʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰ᴍʏ ɢʀᴏᴜᴘ ʙᴏᴛ❱", url="https://t.me/SankiRobot")
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴀᴅᴅ ꜱᴀɴᴋɪ ʀᴏʙᴏᴛ ꜰᴏʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰ᴍʏ ɢʀᴏᴜᴘ ʙᴏᴛ❱", url="https://t.me/SankiRobot")
                ]
            ]
        )
   )
   
   @Client.on_message(filters.command("lock") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴀᴅᴅ ꜱᴀɴᴋɪ ʀᴏʙᴏᴛ ꜰᴏʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰ᴍʏ ɢʀᴏᴜᴘ ʙᴏᴛ❱", url="https://t.me/SankiRobot")
                ]
            ]
        )
   )

@Client.on_message(filters.command("unban") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴀᴅᴅ ꜱᴀɴᴋɪ ʀᴏʙᴏᴛ ꜰᴏʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰ᴍʏ ɢʀᴏᴜᴘ ʙᴏᴛ❱", url="https://t.me/SankiRobot")
                ]
            ]
        )
   )