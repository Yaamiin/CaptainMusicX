import os
import requests
import aiohttp
import youtube_dl

from pyrogram import filters, Client
from youtube_search import YoutubeSearch

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command('song') & ~filters.private & ~filters.channel)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🌺𝗙𝗶𝗻𝗱𝗶𝗻𝗴 𝗧𝗵𝗲 𝗦𝗼𝗻𝗴 ⭐ 𝗙𝗼𝗿𝗺 𝗦𝗲𝗿𝘃𝗲𝗿...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "🌋𝗦𝗼𝗻𝗴 𝗡𝗼𝘁 🌹𝗙𝗼𝘂𝗻𝗱."
        )
        print(str(e))
        return
    m.edit("𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗦𝗼𝗻𝗴 🌺 𝗙𝗿𝗼𝗺 𝗦𝗲𝗿𝘃𝗲𝗿...")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '**🎵 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 :- ✨ @Prayagraj_Op ❤️☝️**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('🌸𝗛𝗲𝘅𝗼𝗿 𝗡𝗼𝘁 𝗚𝗶𝘃𝗲 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝗙𝗼𝗿 𝗚𝗶𝘃𝗶𝗻𝗴 𝗬𝗼𝘂 💿 𝗦𝗼𝗻𝗴 𝗙𝗿𝗼𝗺 𝗦𝗲𝗿𝘃𝗲𝗿')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
