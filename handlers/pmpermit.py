from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"⚡-'ʜᴇʟʟᴏ\n⭐ʜᴇʀᴇ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ ᴏꜰ ꜱᴍᴏᴋᴇʀ ᴍᴜꜱɪᴄ ʙᴏᴛ\n🌼ꜰᴏʀ ʜᴇʟᴘ ᴅᴍ - @Sanki_Owner\n🌺ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ - @\n🌸ᴅᴏɴᴛ ꜱᴘᴀᴍ ʜᴇʀᴇ\n🌠ʜᴇxᴏʀ xᴅ <3\n🌠ꜱᴍᴏᴋᴇʀ xᴅ<3\n")
  return                        
