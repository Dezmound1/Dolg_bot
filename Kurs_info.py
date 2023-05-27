from aiogram import types
from Module import dp
import KB_info
import KB
import cfg




async def get_info_your_kuses(callback: types.CallbackQuery):
    await callback.message.edit_text('Пример ваших курсов\nТипо список курсов', reply_markup= KB_info.back_end_of_registering)


async def def_for_back(callback: types.CallbackQuery):
    await callback.message.edit_text(cfg.message_for_student, reply_markup= KB.end_but)










def KURS_info_hendlers():
    dp.register_callback_query_handler(get_info_your_kuses, text= 'info', state=None)
    dp.register_callback_query_handler(def_for_back, text='back_end', state=None)
