from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import callback_query
from aiogram.utils.callback_data import *
from Module import dp, bot, KB
import re
import cfg
import KB_info
import sql
import fun
import json









class student_FSM(StatesGroup):
    subject = State()
    FSMinfo = State()
    groupe = State()
    name = State()
    number = State()
    birth = State()
    passport_num = State()
    passport_give = State()
    passport_date = State()
    passport_code = State()
    passport_addres = State()




#@dp.message_handler(NUM())
#async def check_NUM(msg: types.Message) -> None:
 #   await None


@dp.message_handler(commands=['cancel'])
async def cmd_cancel(message: types.Message, state= FSMContext):
    await state.finish()
#    await callback.message.answer('Вы вернулись назад', reply_markup=KB.Stud_hello)
async def cmd_cancel2(callback: types.CallbackQuery, state = FSMContext):
    await state.finish()
    await callback.message.answer('Вы вернулись назад', reply_markup=KB.Stud_hello)
async def cmd_cancel3(callback: types.CallbackQuery, state = FSMContext):
    await student_FSM.FSMinfo.set()
    await callback.message.answer('Вы вернулись назад', reply_markup=KB_info.function_for_stud)




async def subject_FSM(callback: types.CallbackQuery, state= student_FSM.subject):
    async with state.proxy() as data:
        data['subject_info'] = fun.subjects_dict[int(callback.data)] # переписать обращение к json
        data['subject_callback'] = callback.data
    if sql.db_profile_exist(callback.from_user.id, data['subject_info']):
        await callback.message.edit_text("Вы уже записывались на этот крус, хотите перезаписаться?", reply_markup= KB.Qwestion_butt)
    else:
        await callback.message.edit_text('Предлагаем выбрать один из следующих вариантов: ', reply_markup=KB_info.function_for_stud)
        await student_FSM.next()

# print('this is ', fun.subjects_dict)
# print(fun.subjects_dict[3])





async def answer_yes(callback: types.CallbackQuery, state= student_FSM.subject):
    await callback.message.edit_text('Предлагаем выбрать один из следующих вариантов: ', reply_markup= KB_info.function_for_stud)
    await student_FSM.next()

async def answer_no(callback: types.CallbackQuery, state= student_FSM.subject):
    await callback.message.answer("Выбирете другой курс!", reply_markup= KB.KB_subject_info)
    await subject_FSM()



async def date_time(callback: types.CallbackQuery, state= student_FSM.FSMinfo):
    async with state.proxy() as data:
        data["data_type"] = callback.data
    with open("data.json", 'r', encoding='utf-8') as file:
        turn_on = json.load(file) # переименовать
        take = turn_on[data['subject_callback']]["schedule"]
    await callback.message.edit_text(f'Информация о <b>дате проведения курса</b> {data["subject_info"]}\nКурс будет проводиться {take} ', reply_markup= KB_info.back_to_function_for_stud )


async def cost(callback: types.CallbackQuery, state= student_FSM.FSMinfo):
    async with state.proxy() as data:
        data["data_type"] = callback.data
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        take = turn_on[data['subject_callback']]["cost"]
    await callback.message.edit_text(f'Информация о <b>стоимости курса</b> {data["subject_info"]}\nКурс стоит: {take} рублей', reply_markup=KB_info.back_to_function_for_stud)

async def num(callback: types.CallbackQuery, state= student_FSM.FSMinfo):
    async with state.proxy() as data:
        data["data_type"] = callback.data
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        take = turn_on[data['subject_callback']]["room"]
    await callback.message.edit_text(f'Информация о <b>номере аудитории курса</b> {data["subject_info"]}\nКурс будет проходить в аудитории: {take}', reply_markup=KB_info.back_to_function_for_stud)

async def teacher(callback: types.CallbackQuery, state= student_FSM.FSMinfo):
    async with state.proxy() as data:
        data["data_type"] = callback.data
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        take = turn_on[data['subject_callback']]["teacher"]
    await callback.message.edit_text(f'Информация о <b>преподавателе</b> {data["subject_info"]}\nКурс проводит: {take}', reply_markup=KB_info.back_to_function_for_stud)

async def comment(callback: types.CallbackQuery, state= student_FSM.FSMinfo):
    async with state.proxy() as data:
        data["data_type"] = callback.data
    with open("data.json", 'r', encoding='utf-8') as hf:
        turn_on = json.load(hf)
        take = turn_on[data['subject_callback']]["comment"]
    await callback.message.edit_text(f'<b>Актуальная информация курса</b> {data["subject_info"]}\n{take}', reply_markup=KB_info.back_to_function_for_stud)



#Процесс регистрации
async def load_kurs(callback: types.CallbackQuery, state= student_FSM.FSMinfo):
    await callback.message.edit_text (f'👉<b>Убедительная просьба, вводить корректную информацию во избежание повторной регистрации</b>👈'
                                      f'\n\nУкажите пожалуйста свою группу!\nПример заполнения данных: БИН-19-2, БТЛ-22-ЖМ1')
    await student_FSM.next()


async def groupe_FSM(message: types.Message, state=student_FSM.groupe):
    async with state.proxy() as data:
        data['num_groupe'] = message.text
    # print(f"{data['num_groupe']}")
    await message.answer('Укажите пожалуйста свое ФИО! Пример заполнения данных:\nИванов Иван Иванович')

    await student_FSM.next()


async def cmd_signal(message: types.Message, state=student_FSM.name):
    name = re.fullmatch(r'(\w{2,})+[ ]+(\w{2,})+[ ]+(\w{2,})', message.text)
    if name:
        async with state.proxy() as data:
            data['name'] = message.text
        await bot.send_sticker(message.from_user.id,
                                       sticker= "CAACAgIAAxkBAAIj2GP_S3KDjec7QiMVaphLRRgaWNsxAAJBAAMoD2oU8OnTI3UcRmEuBA")
        await message.answer(f"Прекрасно, {data['name']}\n Укажите свой номер телефона!\nПример заполнения данных: +79123456789, либо 89123456789")
        await bot.send_sticker(message.from_user.id,
                                       sticker= "CAACAgIAAxkBAAIj2mP_TBhyuzKOf8s5_ZKXP2_ZIDUeAAI_AAMoD2oUaqAv_15u_XkuBA")
        await student_FSM.next()

    else:
        await message.answer("Введите корректно ФИО, образец выше!")


async def number_FSM(message: types.Message, state=student_FSM.number):

    match = re.fullmatch(r'(([+]+79)|89)+\d{9}', message.text)
    if match:
        async with state.proxy() as data:
            data['number'] = message.text
        await message.answer(f"{data['name']}, Укажите дату вашего рождения!\nПример ввода данных: DD.MM.YYYY")
        await student_FSM.next()

    else:
        await message.answer("Введите корректный номер телефона, образец ввода вы можете увидеть выше.")


async def date_of_birth(message: types.Message, state=student_FSM.birth): #datetime
    date = re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+(200+[0-8])', message.text)
    if date:
        async with state.proxy() as data:
            data['date_birth'] = message.text
        await message.answer(f"И снова победа, {data['name']}, теперь давай оформим на тебя кредит!\n Укажи свои паспортные данные!\nДля начала введи серию и номер!\nПример: 2025 126661")
        await student_FSM.next()
    else:
        await message.answer('Пожалуйста, введите данные корректно!')



async def passport_NUM_FSM(message: types.Message, state=student_FSM.passport_num): #серия и номер паспорта
    num = re.fullmatch(r'(\d{2})+(\d{2})+[ ]+(\d{6})', message.text)
    if num:
         async with state.proxy() as data:
            data['passport_NUM'] = message.text
         await message.answer(f"Прекрасно, {data['name']}, укажите кем был выдан пасспорт!") #форму заполнения!
         await student_FSM.next()
    else:
        await message.answer("Неверно указаны данные, попробуйте еще раз")




async def passport_GIVE_FSM(message: types.Message, state=student_FSM.passport_give): #данные о выдачи пасспорта

    async with state.proxy() as data:
        data['passport_GIVE'] = message.text
    await  message.answer("Укажи дату выдачи пасспортных данных!\nПример ввода данных: DD.MM.YYYY")
    await student_FSM.next()




async def passport_DATE_FSM(message: types.Message,state= student_FSM.passport_date): #указать ыалидность года !!!
    date = re.fullmatch(r'(([0-2][1-9])|3+[0-1])+[.]+((0+[1-9])|[10-12])+[.]+((201+[5-9])|(202+[0-5]))', message.text)
    if date:
        async with state.proxy() as data:
            data['passport_DATE'] = message.text
        await message.answer("Укажите код подразделения, выдавшего документ!!\nПример данных: 250-006")
        await student_FSM.next()
    else:
        await message.answer("Укажите данные согласно примеру выше!")




async def passport_CODE_FSM(message: types.Message,state= student_FSM.passport_code):
    code = re.fullmatch(r'(\d{3})+[-]+(\d{3})', message.text)
    if code:
        async with state.proxy() as data:
            data['passport_CODE'] = message.text
        await message.answer("Укажите адрес места регистрации!\nФормат заполнения: Страна, область, город, населенный пункт(если есть), улица, дом.")
        await student_FSM.next()
    else:
        await message.answer("Укажите данные согласно примеру выше!")




async def passport_ADRES_FSM(message: types.Message, state=student_FSM.passport_addres): # общая рабочая модель получения паспортных данных
    async with state.proxy() as data:
        data['passport_ADRES'] = message.text
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAIj3GP_VJcD_TNq8yvS7B5V3iejLPpuAAKNFgACHBsoSM3ElsDvm8gELgQ"
                           )

    await state.finish()
    # print(f"{data['subject_info']} ,{data['num_groupe']} ,{data['name']} ,{data['number'].strip('+')},{data['date_birth'].replace('.','')} , {data['passport_NUM'].replace(' ','')} ,{data['passport_GIVE']}, {data['passport_DATE'].replace('.','')} , {data['passport_CODE'].replace('-','')} ,{data['passport_ADRES']}")
    if sql.db_profile_exist(message.from_user.id, data['subject_info']):
        await message.answer("Мы перезаписали ваши данные")
    else:
        sql.db_profile_insertone({"id": message.from_user.id,
                                  'grup_name': data['num_groupe'],
                                  'fio': data['name'],
                                  'phone': data['number'].strip('+'),
                                  'date_bith': data['date_birth'].replace('.',''),
                                  'passport': data['passport_NUM'].replace(' ',''),
                                  'kem_vid': data['passport_GIVE'],
                                  'date_pas': data['passport_DATE'].replace('.',''),
                                  'kod_pod': data['passport_CODE'].replace('-',''),
                                  'reg_reg': data['passport_ADRES'],
                                  'subject': data['subject_info']})

    await message.answer(cfg.message_for_student, reply_markup= KB.end_but)


# async with state.proxy() as data:
#     data['edit_info'] = message.text
# print(data['edit_info'])
# with open("data.json", 'r', encoding='utf-8') as hf:
#     turn_on = json.load(hf)




def FSM_hendlers():

    dp.register_message_handler(cmd_cancel, commands= 'cancel', state= '*')
    dp.register_callback_query_handler(answer_yes, text='Yes', state= student_FSM.subject)
    dp.register_callback_query_handler(answer_no, text='No', state= student_FSM.subject)
    dp.register_callback_query_handler(cmd_cancel2, text= 'back_from_list', state= '*')
    dp.register_callback_query_handler(cmd_cancel3, text='back_is_all', state = '*')
    dp.register_callback_query_handler(subject_FSM, state= student_FSM.subject)
    dp.register_callback_query_handler(load_kurs, text='kurs', state= student_FSM.FSMinfo)
    dp.register_callback_query_handler(date_time, text='date_time', state= student_FSM.FSMinfo)
    dp.register_callback_query_handler(cost, text= 'cost', state= student_FSM.FSMinfo)
    dp.register_callback_query_handler(num, text='num', state= student_FSM.FSMinfo)
    dp.register_callback_query_handler(teacher, text='teacher', state= student_FSM.FSMinfo)
    dp.register_callback_query_handler(comment, text='comment', state= student_FSM.FSMinfo)
    dp.register_message_handler(groupe_FSM, state= student_FSM.groupe)
    dp.register_message_handler(cmd_signal, state= student_FSM.name)
    dp.register_message_handler(number_FSM, state= student_FSM.number)
    dp.register_message_handler(date_of_birth, state= student_FSM.birth)
    dp.register_message_handler(passport_NUM_FSM, state= student_FSM.passport_num)
    dp.register_message_handler(passport_GIVE_FSM, state= student_FSM.passport_give)
    dp.register_message_handler(passport_DATE_FSM, state= student_FSM.passport_date)
    dp.register_message_handler(passport_CODE_FSM, state= student_FSM.passport_code)
    dp.register_message_handler(passport_ADRES_FSM, state=student_FSM.passport_addres)

