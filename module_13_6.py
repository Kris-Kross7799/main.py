from aiogram import Bot,Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


api=""
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())

ikb=InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
ibt=InlineKeyboardButton(text='Формулы рассчёта', callback_data='formulas')
ibt2=InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')

ikb.add(ibt)
ikb.insert(ibt2)

class UserState(StatesGroup):
    age=State()
    growth=State()
    weight=State()
    sex=State()

@dp.message_handler(commands=["start"])
async def all_message(message):
    await message.answer("Привет, я - бот, помогающий Твоему здоровью!\n"
                         "Выберите опцию", reply_markup=ikb)

@dp.callback_query_handler(text="formulas")
async def formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()   #команда, заверщающая вызов и делающая
    # кнопку снова активной

@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer("ведите свой возраст")
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=float(message.text))
    await message.answer("Введите свой рост в см")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=float(message.text))
    await message.answer("Введите свой вес в кг")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_sex(message, state):
    await state.update_data(weight=float(message.text))
    await message.answer("Введите свой пол (м или ж)")
    await UserState.sex.set()

@dp.message_handler(state=UserState.sex)
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    data = await state.get_data()
    age=data['age']
    growth=data['growth']
    weight=data['weight']
    sex=data['sex']
    if sex=='м' or sex=="М" or sex=='m' or sex=='M':
        result=10.0*weight+6.25*growth-5.0*age+5
    else:
        result = 10.0 * weight + 6.25 * growth - 5.0 * age -161
    await message.answer(f"Ваша норма калорий {result} в день")
    await state.finish()

@dp.message_handler(text=["Информация"])
async def info(message):
    await message.answer("Раздел в разработке...")

@dp.message_handler()
async def start(message):
    await message.answer("Добро пожаловать! Рады видеть Вас, "
                         "для начала введите команду /start")


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)