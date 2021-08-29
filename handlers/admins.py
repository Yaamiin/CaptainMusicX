from asyncio.queues import QueueEmpty
from cache.admins import set
from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic
from queues import queues
import traceback
import os
import sys
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import filters, emoji
from config import BOT_USERNAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from config import que, admins as a

@Client.on_message(filters.command('reload'))
async def update_admin(client, message):
    global a
    admins = await client.get_chat_members(message.chat.id, filter="administrators")
    new_ads = []
    for u in admins:
        new_ads.append(u.user.id)
    a[message.chat.id] = new_ads
    await message.reply_text('𝗕𝗼𝘁 𝗥𝗲𝗹𝗼𝗮𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹🤞𝗘𝗻𝗷𝗼𝘆 🤨 **{}**'.format(message.chat.title))



@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text("❗ 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗜𝘀 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 ✨")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("▶️ 𝗣𝗮𝘂𝘀𝗲𝗱 😔🤟")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text("❗ 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗜𝘀 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 ✨")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("⏸ 𝗥𝗲𝘀𝘂𝗺𝗲𝗱 ❤️🤟")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗜𝘀 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴 ✨")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("❌𝗦𝘁𝗼𝗽 🛑 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴 ✨")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 😔 𝗜𝘀 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 🎶 𝗧𝗼 𝗦𝗸𝗶𝗽 💫")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("➡️ 𝗦𝗸𝗶𝗽 💫 𝗧𝗵𝗲 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 😊 𝗦𝗼𝗻𝗴 ❤️🤟")
