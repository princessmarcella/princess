from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""π€ Hi {message.from_user.first_name}!

π€ I am ΦΚΙ¨ΥΌΖΙΦΦ ΚΗΚΖΙΚΚΗ. π€

π @me_harry π

π I can play music in your Telegram Group's Voice Chatπ

πΆ WANNA KNOW ABOUT ME. πΆ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Code", url="https://github.com/princessmarcella/princess"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Our Group", url="https://t.me/loveshoveishqzaade"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/me_harry"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "END", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**ΦΚΙ¨ΥΌΖΙΦΦ:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΆ Search πΆ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "β Close β", callback_data="close"
                    )
                ]
            ]
        )
    )
