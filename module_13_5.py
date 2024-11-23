from aiogram import Bot,Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api=""
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())

kb=ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
bt=KeyboardButton(text='Информация')
bt2=KeyboardButton(text='Рассчитать')

kb.add(bt)
kb.insert(bt2)

class UserState(StatesGroup):
    age=State()
    growth=State()
    weight=State()
    sex=State()

@dp.message_handler(commands=["start"])
async def all_message(message):
    await message.answer("Привет, я - бот, помогающий Твоему здоровью!\n"
                         "Для подсчёта суточной нормы калорий нажмите на"
                         "кнопку Рассчитать", reply_markup=kb)

@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer("ведите свой возраст")
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