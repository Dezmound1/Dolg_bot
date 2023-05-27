from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import callback_query
import Module
from aiogram.utils.callback_data import *
from cfg import *
import fun
import json
from aiogram import types

devid = dev_id



Menu = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                text="Авторизоваться как администратор",
                callback_data='admin'
                        )
                ],
                [
                InlineKeyboardButton(
                        text="Авторизоваться как студент",
                        callback_data='hello'
                        )
                ]


        ]
)


Stud_hello = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="Частые вопросы",
                        callback_data='FAQ'
                        )
                ],
                [
                InlineKeyboardButton(
                        text="Посмотреть курсы",
                        callback_data='Get_kurs_info'
                        )
                ]
        ]
)

back_to_stud_hello = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="Вернуться назад",
                        callback_data='retrit'
                        )
                ]
        ]
)

admin_back = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="🧐Вернуться назад🧐",
                        callback_data='cancel_all'
                        )
                ]
        ]
)
admin_question = InlineKeyboardMarkup(row_width= 2, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="✅Да✅",
                        callback_data='Yes'
                        )
                ],
                [
                InlineKeyboardButton(
                        text="❌Нет❌",
                        callback_data='No'
                        )
                ]
        ]
)

admin_choose_step = InlineKeyboardMarkup(row_width=1, resize_keyboard = True,
        inline_keyboard= [
        [
        InlineKeyboardButton(
                text= "Включить/выключить предметы",
                callback_data= "turn_choice"
                )
        ],[
        InlineKeyboardButton(
                text= "Поменять информацию на курсе",
                callback_data= "info_choice"
                )
                ]
        ]
)

admin_turn_me_on = InlineKeyboardMarkup(row_width=1, resize_keyboard = True,
        inline_keyboard= [
        [
        InlineKeyboardButton(
                text="Включенные предметы",
                callback_data= "turn_on"
                )
        ],[
        InlineKeyboardButton(
                text= "Выключенные предметы",
                callback_data= "turn_off"
                )
                ]
        ]

)


buttons_off = []
with open("data.json", 'r', encoding='utf-8') as hf:
        subjects_all = json.load(hf)
        for i in subjects_all:
                if not subjects_all[i]["status"]:
                        buttons_off.append([InlineKeyboardButton(
                                text= subjects_all[i]["title"],
                                callback_data= i)
                        ])
KB_all_buttons_off = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard= buttons_off)

# def buttons():
#         with open('data.json', 'r', encoding='utf-8') as inflow:
#                 scrapy = json.load(inflow)
#                 result = {i['status'] : i['title'] for i in scrapy}

buttons_on = []
with open("data.json", 'r', encoding='utf-8') as hf:
        subjects_all = json.load(hf)
        for i in subjects_all:
                if subjects_all[i]["status"]:
                        buttons_on.append([InlineKeyboardButton(
                                text= subjects_all[i]["title"],
                                callback_data= i)
                        ])
KB_all_buttons_on = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard= buttons_on)

# if callback Да == subjects_all[i]["status"] == true , перезаписываю subjects_all в data.json

KB_state_turn = InlineKeyboardMarkup(row_width=1, resize_keyboard = True,
        inline_keyboard= [
        [
        InlineKeyboardButton(
                text="Включить",
                callback_data= "on"
                )
        ],[
        InlineKeyboardButton(
                text= "Выключить",
                callback_data= "off"
                )
                ]
        ]

)










function = InlineKeyboardMarkup(row_width= 2, resize_keyboard = True,
        inline_keyboard=[
        [
        InlineKeyboardButton(
                text="Стоимость",
                callback_data='cost'
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
        ]
        ]
)


end_but = InlineKeyboardMarkup(row_width=1, resize_keyboard = True,
        inline_keyboard=[
        [
        InlineKeyboardButton(
                text="ваши курсы ",
                callback_data='your_curs'
                )
        ],
                [
        InlineKeyboardButton(
                text="записаться еще",
                callback_data='more'
                )
        ],
        [
        InlineKeyboardButton(
                text="информация по курсу",
                callback_data='info'
                )
        ]
]
)



# c = []
# for i in fun.subjects_dict:
#         c.append([
#                 InlineKeyboardButton(
#                         text= fun.subjects_dict[i],
#                         callback_data= i)
#                        ])

KB_subject_info = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard= buttons_on)


Sure = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="Да",
                        callback_data='Yes'
                        )
                ],
                [
                InlineKeyboardButton(
                        text= "Нет",
                        callback_data= 'No'
                        )
                ]
        ]
)

Menu2 = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="Зарегестрироваться как студент",
                        callback_data= 'ass_stud'
                        )
                ]
        ]
)

Qwestion_butt = InlineKeyboardMarkup(row_width=1, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(
                        text="Да",
                        callback_data= 'Yes'
                        )
                ],
                [
                InlineKeyboardButton(
                        text="Нет",
                        callback_data='No'
                )
                ]
        ]
)