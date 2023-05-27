from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import callback_query
from aiogram.utils.callback_data import *
from Module import dp, bot, KB
import json



class admin_FSM(StatesGroup):
    register_admin = State()
    juicy_choice = State()
    juicy_turn = State()
    state_turn = State()
    edit_subject = State()
    call_to_edit = State()
    choose_edit_cost = State()
    choose_edit_date = State()
    choose_edit_num = State()
    choose_edit_teacher = State()
    choose_edit_comment = State()

    editing = State()
    info_admin = State()
    choose_fun = State()


async def if_stud(callback: types.CallbackQuery, state = FSMContext):
    await callback.message.edit_text("Вы вернулись, как студент", reply_markup= KB.Menu)
    await state.finish()





async def Password_admin(message: types.Message, state= admin_FSM.register_admin):
    if message.text == 'password':
        await message.answer('Преветствую, Даниил, что мы редактируем на этот раз?', reply_markup= KB.admin_choose_step)  # Включить/выключить запись, поменять информацию на курсе (если курс True)
        await admin_FSM.next()
    else:

        await message.answer(
            'Пожалуйста, введите корректный ключ, если вы не администратор, предлагаю зарегестрироваться на курс',
            reply_markup= KB.Menu2)


async def exallent_choice(callback: types.CallbackQuery, state= admin_FSM.juicy_choice):
    await callback.message.edit_text("Выбирите категорию предметов", reply_markup= KB.admin_turn_me_on)
    await admin_FSM.next()

async def juicy_on(callback: types.CallbackQuery, state= admin_FSM.juicy_turn):
    await callback.message.edit_text("Выбирите предмет из включенных", reply_markup= KB.KB_all_buttons_on)    # функция для вызова кнопок со статусом True

async def juicy_off(callback: types.CallbackQuery, state= admin_FSM.juicy_turn):
    await callback.message.edit_text("Выбирите предмет из выключенных", reply_markup= KB.KB_all_buttons_off)    # функция для вызова кнопок со статусом false


async def press_turn_butt(callback: types.CallbackQuery, state= admin_FSM.juicy_turn):
    async with state.proxy() as data:
        data['subject_state_turn'] = callback.data
    await callback.message.edit_text("Включить или выключить этот предмет ?", reply_markup= KB.KB_state_turn)
    print(data['subject_state_turn'])
    await admin_FSM.next()

async def state_turn(callback: types.CallbackQuery, state= admin_FSM.state_turn):
    async with state.proxy() as data:
        data["data_type"] = callback.data
    if callback.data == 'on':
        with open("data.json", 'r', encoding='utf-8') as hf:
            turn_on = json.load(hf)
            turn_on[data['subject_state_turn']]["status"] = True

            KB.buttons()


        with open("data.json", 'w', encoding='utf-8') as hf:
            json.dump(turn_on, hf, indent=4, ensure_ascii= False)
        await callback.message.edit_text("Вы успешно включили кнопку!", reply_markup=KB.admin_choose_step)
        await admin_FSM.juicy_choice.set()
    if callback.data == 'off':
        with open("data.json", 'r', encoding='utf-8') as hf:
            turn_off = json.load(hf)
            turn_off[data['subject_state_turn']]["status"] = False
        with open("data.json", 'w', encoding='utf-8') as hf:
            json.dump(turn_off, hf, indent=4, ensure_ascii= False)
        await callback.message.edit_text("Вы успешно выключили кнопку!", reply_markup=KB.admin_choose_step)
        await admin_FSM.juicy_choice.set()




async def choose_lesson(callback: types.CallbackQuery, state= admin_FSM.info_admin):
    async with state.proxy() as data:
        data["editor"] = callback.data
    print(f"{data['editor']}")
    await callback.message.edit_text("Выбирете раздел, ктороый нужно отредактировать, или вернитесь назад!", reply_markup= KB.function)
    await admin_FSM.next()

 #Функции для обработки информации
async def date_time(callback: types.CallbackQuery, state= admin_FSM.choose_fun):
    async with state.proxy() as data:
        data["function"] = callback.data
    print(f"{data['function']}")
    await callback.message.edit_text("Изменить дату предмета", reply_markup=KB.admin_back)
    await admin_FSM.next()


async def cost(callback: types.CallbackQuery, state=admin_FSM.choose_fun):
    async with state.proxy() as data:
        data["function"] = callback.data
    print(f"{data['function']}")
    await callback.message.edit_text("Изменить стоимость курса", reply_markup=KB.admin_back)
    await admin_FSM.next()

async def num(callback: types.CallbackQuery, state=admin_FSM.choose_fun):
    async with state.proxy() as data:
        data["function"] = callback.data
    print(f"{data['function']}")
    await callback.message.edit_text("Изменить номер аудитории курса", reply_markup=KB.admin_back)
    await admin_FSM.next()

async def teacher(callback: types.CallbackQuery, state=admin_FSM.choose_fun):
    async with state.proxy() as data:
        data["function"] = callback.data
    print(f"{data['function']}")
    await callback.message.edit_text("Изменить преподавателя курса", reply_markup= KB.admin_back)
    await admin_FSM.next()

async def comment(callback: types.CallbackQuery, state=admin_FSM.choose_fun):
    async with state.proxy() as data:
        data["function"] = callback.data
    print(f"{data['function']}")
    await callback.message.edit_text("Изменить актуальную информацию курса", reply_markup= KB.admin_back)
    await admin_FSM.next()

async def dolg_list(callback: types.CallbackQuery, state=admin_FSM.choose_fun):
    async with state.proxy() as data:
        data["function"] = callback.data
    print(f"{data['function']}")
    await callback.message.edit_text("Посмотреть список должников по курсу", reply_markup= KB.admin_back)
    await admin_FSM.next()

async def count(callback: types.CallbackQuery, state=admin_FSM.choose_fun):
    async with state.proxy() as data:
        data["function"] = callback.data
    print(f"{data['function']}")
    await callback.message.edit_text("Посмотреть кол-во должников по курсу", reply_markup= KB.admin_back)
    await admin_FSM.next()




async def get_on_subjects(callback: types.CallbackQuery, state= admin_FSM.juicy_choice):
    await callback.message.edit_text("Выберете предмет, в котором вы хотите изменить информацию", reply_markup= KB.KB_all_buttons_on)
    await admin_FSM.edit_subject.set()


async def edit_info(callback: types.CallbackQuery, state= admin_FSM.edit_subject):
    async with state.proxy() as data:
        data['subjects_info'] = callback.data
    print(data['subjects_info'])
    await callback.message.edit_text("Какую инфу меняем ?", reply_markup= KB.function)
    await admin_FSM.next()





# Изменение даты
async def call_to_date(callback: types.CallbackQuery, state= admin_FSM.call_to_edit):
    await callback.message.edit_text("Изменение даты предмета, введите данные:")
    await admin_FSM.choose_edit_date.set()

async def choose_date(message: types.Message, state= admin_FSM.choose_edit_date):
    async with state.proxy() as data:
        data['edit_info'] = message.text
    print(data['edit_info'])
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        turn_on[data['subjects_info']]["schedule"] = message.text
    with open("data.json", 'w', encoding='utf-8') as hf:
        json.dump(turn_on, hf, indent=4, ensure_ascii=False)
    await message.answer("Какую инфу меняем ?", reply_markup= KB.function)
    await admin_FSM.call_to_edit.set()


# Изменение стоимости предмета
async def call_to_cost(callback: types.CallbackQuery, state= admin_FSM.call_to_edit):
    await callback.message.edit_text("Изменение стоимости предмета, введите данные:")
    await admin_FSM.choose_edit_cost.set()


async def choose_cost(message: types.Message, state= admin_FSM.choose_edit_cost):
    async with state.proxy() as data:
        data['edit_info'] = message.text
    print(data['edit_info'])
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        turn_on[data['subjects_info']]["cost"] = message.text
    with open("data.json", 'w', encoding='utf-8') as hf:
        json.dump(turn_on, hf, indent=4, ensure_ascii=False)
    await message.answer("Какую инфу меняем ?", reply_markup= KB.function)
    await admin_FSM.call_to_edit.set()




# Изменение номера аудитории
async def call_to_num(callback: types.CallbackQuery, state= admin_FSM.call_to_edit):
    await callback.message.edit_text("Изменение проведения занятий по предмету, введите номер аудитории:")
    await admin_FSM.choose_edit_num.set()

async def choose_num(message: types.Message, state= admin_FSM.choose_edit_num):
    async with state.proxy() as data:
        data['edit_info'] = message.text
    print(data['edit_info'])
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        turn_on[data['subjects_info']]["room"] = message.text
    with open("data.json", 'w', encoding='utf-8') as hf:
        json.dump(turn_on, hf, indent=4, ensure_ascii=False)
    await message.answer("Какую инфу меняем ?", reply_markup= KB.function)
    await admin_FSM.call_to_edit.set()


# Изменение информации о преподавателе
async def call_to_teacher(callback: types.CallbackQuery, state= admin_FSM.call_to_edit):
    await callback.message.edit_text("Впишите ФИО преподавателя, проводящего предмет:")
    await admin_FSM.choose_edit_teacher.set()

async def choose_teacher(message: types.Message, state= admin_FSM.choose_edit_teacher):
    async with state.proxy() as data:
        data['edit_info'] = message.text
    print(data['edit_info'])
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        turn_on[data['subjects_info']]["teacher"] = message.text
    with open("data.json", 'w', encoding='utf-8') as hf:
        json.dump(turn_on, hf, indent=4, ensure_ascii=False)
    await message.answer("Какую инфу меняем ?", reply_markup= KB.function)
    await admin_FSM.call_to_edit.set()



# Изменение коментария к предмету
async def call_to_comment(callback: types.CallbackQuery, state= admin_FSM.call_to_edit):
    await callback.message.edit_text("Добавьте комментарий:")
    await admin_FSM.choose_edit_comment.set()

async def choose_comment(message: types.Message, state= admin_FSM.choose_edit_comment):
    async with state.proxy() as data:
        data['edit_info'] = message.text
    print(data['edit_info'])
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        turn_on[data['subjects_info']]["comment"] = message.text
    with open("data.json", 'w', encoding='utf-8') as hf:
        json.dump(turn_on, hf, indent=4, ensure_ascii=False)
    await message.answer("Какую инфу меняем ?", reply_markup= KB.function)
    await admin_FSM.call_to_edit.set()










def FSMlist_hendlers():
    # dp.callback_query_handler(from_signal, state= admin_FSM.edit)
    dp.register_message_handler(Password_admin, state= admin_FSM.register_admin)
    dp.register_callback_query_handler(get_on_subjects, text= 'info_choice', state= admin_FSM.juicy_choice)
    dp.register_callback_query_handler(edit_info, state= admin_FSM.edit_subject)
    dp.register_callback_query_handler(call_to_cost, text ='cost', state= admin_FSM.call_to_edit)
    dp.register_callback_query_handler(call_to_date, text ='date_time', state= admin_FSM.call_to_edit)
    dp.register_callback_query_handler(call_to_num, text ='num', state= admin_FSM.call_to_edit)
    dp.register_callback_query_handler(call_to_teacher, text ='teacher', state= admin_FSM.call_to_edit)
    dp.register_callback_query_handler(call_to_comment, text ='comment', state= admin_FSM.call_to_edit)


    dp.register_message_handler(choose_cost, state= admin_FSM.choose_edit_cost)   # Здесь дописывать
    dp.register_message_handler(choose_date, state= admin_FSM.choose_edit_date)
    dp.register_message_handler(choose_num, state= admin_FSM.choose_edit_num)
    dp.register_message_handler(choose_teacher, state= admin_FSM.choose_edit_teacher)
    dp.register_message_handler(choose_comment, state= admin_FSM.choose_edit_comment)


    dp.register_callback_query_handler(exallent_choice, text='turn_choice', state= admin_FSM.juicy_choice)
    dp.register_callback_query_handler(juicy_on, text="turn_on", state= admin_FSM.juicy_turn)
    dp.register_callback_query_handler(juicy_off, text="turn_off", state= admin_FSM.juicy_turn)
    dp.register_callback_query_handler(press_turn_butt, state= admin_FSM.juicy_turn)
    dp.register_callback_query_handler(state_turn, state= admin_FSM.state_turn)
    dp.register_callback_query_handler(choose_lesson, state = admin_FSM.info_admin)
    dp.register_callback_query_handler(if_stud, text= 'ass_stud', state= '*')
    dp.register_callback_query_handler(date_time, text='date_time', state= admin_FSM.choose_fun)
    dp.register_callback_query_handler(cost, text='cost', state= admin_FSM.choose_fun)
    dp.register_callback_query_handler(num, text='num', state= admin_FSM.choose_fun)
    dp.register_callback_query_handler(teacher, text='teacher', state= admin_FSM.choose_fun)
    dp.register_callback_query_handler(comment, text='comment', state= admin_FSM.choose_fun)
    dp.register_callback_query_handler(dolg_list, text='list', state= admin_FSM.choose_fun)
    dp.register_callback_query_handler(count, text='count', state= admin_FSM.choose_fun)

