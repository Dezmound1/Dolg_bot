import types

from aiogram import executor

import FSM

from cfg import *
from FSM import *
import FSMlist
from FSMlist import *
from Module import dp
import KB
import KB_info

import Kurs_info






FSM.FSM_hendlers()
FSMlist.FSMlist_hendlers()
Kurs_info.KURS_info_hendlers()







async def on_startup(_):
    print("Ура, я в деле!")


@dp.callback_query_handler(text='Get_kurs_info')
async def GET_kurs_info(callback: types.CallbackQuery):
    await callback.message.edit_text(cfg.info_about_kurs, reply_markup= KB.KB_subject_info)
    await student_FSM.subject.set()



@dp.callback_query_handler(text='more')
async def more_stud(callback: types.CallbackQuery):
    await callback.message.answer(cfg.again,
                                  reply_markup=KB.KB_subject_info)
    await student_FSM.subject.set()


@dp.callback_query_handler(text= 'hello')
async def hello_for_stud(callback: types.CallbackQuery):
    await callback.message.answer(hello_stud, reply_markup= KB.Stud_hello)


@dp.callback_query_handler(text= 'FAQ')
async def FAQ_for_stud(callback: types.CallbackQuery):
    await callback.message.edit_text(faq, reply_markup = KB.back_to_stud_hello)

@dp.callback_query_handler(text= 'retrit')
async def FAQ_for_stud(callback: types.CallbackQuery):
    await callback.message.edit_text(hello_stud, reply_markup = KB.Stud_hello)




# #КОЛБЭК В ФСМ ПО СТУД
# @dp.callback_query_handler(text='signal')
# async def load_for_kurs(callback: types.CallbackQuery):
#     await callback.message.edit_text("Вы уверены, что хотите записаться на <b>Теорию сигналов</b>?", reply_markup= KB.Sure)
#     await student_FSM.subject.set()





@dp.callback_query_handler(text='cancel_all_from_admin')
async def load_for_admin(callback: types.CallbackQuery):
        await callback.message.edit_text("Вы можете выбрать действие еще раз", reply_markup= KB.Menu)


@dp.callback_query_handler(text='admin')
async def load_for_admin(callback: types.CallbackQuery):
        await callback.message.answer(For_admin, reply_markup= None)
        await admin_FSM.register_admin.set()






# @dp.callback_query_handler(text='a_signal')
# async def editor_signal(callback: types.CallbackQuery):
#     await callback.message.edit_text("Что мы меняем здесь?", reply_markup= KB.function)
#
#
#
# @dp.callback_query_handler(text='a_C_shit')
# async def editor_signal(callback: types.CallbackQuery):
#     await callback.message.edit_text("Что мы меняем здесь?", reply_markup= KB.function)
#
#
# @dp.callback_query_handler(text='a_OOP')
# async def editor_signal(callback: types.CallbackQuery):
#     await callback.message.edit_text("Что мы меняем здесь?", reply_markup= KB.function)
#
#
# @dp.callback_query_handler(text='a_java')
# async def editor_signal(callback: types.CallbackQuery):
#     await callback.message.edit_text("Что мы меняем здесь?", reply_markup= KB.function)
#



@dp.message_handler(commands= ['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать в нашего бота',
                         reply_markup= KB.Menu)



#БЭКИ ДЛЯ ИНФЫ ПО ЛИНИИ СТУДЕНТОВ
@dp.callback_query_handler(text='cancel_all_from_info')
async def BACK_from_info(callback: types.CallbackQuery):
    await callback.message.edit_text(cfg.info_about_kurs, reply_markup=KB.KB_subject_info)






if __name__ == "__main__":
	executor.start_polling(dp,
                           on_startup= on_startup,
                           skip_updates=True)