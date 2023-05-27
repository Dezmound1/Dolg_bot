from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import callback_query
import Module
from aiogram.utils.callback_data import *
from cfg import *


from aiogram import types

devid = dev_id






function_for_stud = InlineKeyboardMarkup(row_width=1, resize_keyboard = True,
        inline_keyboard=[
        [
        InlineKeyboardButton(
            text= f"📖ЗАПИСАТЬСЯ на курс📖" ,
                callback_data='kurs'
                 )
        ],
        [
        InlineKeyboardButton(
                text="Рассписание",
                callback_data='date_time'
                )
        ],
                [
        InlineKeyboardButton(
                text="Стоимость",
                callback_data='cost'
                )
        ],
        [
        InlineKeyboardButton(
                text="Номер аудитории",
                callback_data='num'
                )
        ],
        [
        InlineKeyboardButton(
                text="Преподаватель",
                callback_data='teacher'
                )
        ],
        [
        InlineKeyboardButton(
                text="Коментарий",
                callback_data='comment'
                )
        ],
        [
        InlineKeyboardButton(
                text="⏮Вернуться назад⏮",
                callback_data='back_from_list'
                )
        ]
        ]
)


#КНОПКИ НАЗАД ИЗ РАЗДЕЛА ИНФО

back_to_function_for_stud = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="⏮Вернуться назад⏮",
                        callback_data='back_is_all'
                        )
                ]
        ]
)

