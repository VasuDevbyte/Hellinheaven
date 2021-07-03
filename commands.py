#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = "┈••✿@Explore_Cinema✿••\n\n➠ Series Channel : https://t.me/Series_Terminal_Channel\n\n➠Group : https://t.me/Series_Terminal\n\nWe aRe So Glad For Using Thiz Bot 🖤\n\n <b>Must InForm Your Frnds By Sharing</b>\n\n By Sharing..!"
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Share 🥲', url="https://t.me/share/url?url=💯%20𝙽𝙾%201%20𝙼𝙾𝚅𝙸𝙴%20𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙸𝙽𝙶%20𝙶𝚁𝙾𝚄𝙿%20𝙸𝙽%20𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼%20✅%20%0A%0A𝙹𝙾𝙸𝙽%20𝙰𝙽𝙳%20𝚁𝙴𝚀%20𝚈𝙾𝚄𝚁%20𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴%20𝙼𝙾𝚅𝙸𝙴𝚂%20𝚁𝙸𝙶𝙷𝚃%20𝙽𝙾𝚆%20%0A%0A💠%20➠%20𝙶𝚁𝙾𝚄𝙿%20:-%20@Explore_cinema%20%0A💠%20➠%20ForSeries%20:-%20@Series_Terminal_Channel%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@Series_Terminal"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Share 🤞', url="https://t.me/share/url?url=💯%20𝙽𝙾%201%20𝙼𝙾𝚅𝙸𝙴%20𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙸𝙽𝙶%20𝙶𝚁𝙾𝚄𝙿%20𝙸𝙽%20𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼%20✅%20%0A%0A𝙹𝙾𝙸𝙽%20𝙰𝙽𝙳%20𝚁𝙴𝚀%20𝚈𝙾𝚄𝚁%20𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴%20𝙼𝙾𝚅𝙸𝙴𝚂%20𝚁𝙸𝙶𝙷𝚃%20𝙽𝙾𝚆%20%0A%0A💠%20➠%20𝙶𝚁𝙾𝚄𝙿%20:-%20@Explore_cinema%20%0A💠%20➠%20ForSeries%20:-%20@Series_Terminal_Channel%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@Series_Terminal"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'MasTer', url="https://t.me/mrvasuz"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('MasTer👑', url='https://t.me/mrvasuz'),
        InlineKeyboardButton('Eeva..🤕', url ='https://t.me/Explore_Cinema')
    ],[
        InlineKeyboardButton('Questions?😏', url='https://www.google.com')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
