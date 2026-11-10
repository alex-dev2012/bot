
from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

# стартовая клавиатура для пользователя с разными кнопками
start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='➕Записаться к мастеру', callback_data='note'), InlineKeyboardButton(text='❌Отмена записи', callback_data='cancel')],
    [InlineKeyboardButton(text='💲Прайс-лист', callback_data='price-list'), InlineKeyboardButton(text='🧰Портфолио', callback_data='portfolio')],
    [InlineKeyboardButton(text='👤Админ-панель', callback_data='admin')]
])
# клавиатура для вызова меню шаг назад
back_to_start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️Назад', callback_data='back_to_start')]
])
