import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6aa58247f23fd76034c9.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = [â¨ ððð¡ð¢ ððð§ð â¤ï¸](https://t.me/Itz_Venom_xD)

ðð«ððð­ð¨ð« :- [â¨ ððð¡ð¢ ððð§ð](https://t.me/Itz_Venom_xD)
ðð°ð§ðð« :- [â¨ â-ðð«ð¬'ððð§ðð²](https://t.me/Candy_626)
ðð¢ð¬ðð®ð¬ð¬ :- [â¨  ðð¨ðð¤ð¬ ð§](https://t.me/Shayri_Music_Lovers)
ðð¨ð®ð«ðð  :- [â¨  ðð¹ð¶ð°ð¸ âï¸ ð¥ð²ð½ð¼ ð](https://github.com/CandyMusic/CandyPrivateMusic)
ðð¡ðð§ð§ðð¥ :- [â¨ðð¹ð¶ð°ð¸ âï¸ ð¡ð¼ð ð©](https://t.me/Shayri_Music_Lovers)
ðð®ð©ð©ð¨ð«ð­ :- [â¨ ðð¼ð¶ð» â¤ï¸ð¥](https://t.me/AlishaSupport)

ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [â-ðð«ð¬'ððð§ðð² ð¬](https://t.me/Candy_626)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â â° Aá´á´ Má´ Tá´ Yá´á´Ê GÊá´á´á´ â± â", url=f"https://t.me/CandyMusic_Robot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/218b5b460d60e7ea68831.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ ðð¥ð¢ðð¤ ððð©ð¨ ð", url=f"https://github.com/CandyMusic/candyMusicPlayer")
                ]
            ]
        ),
    )
