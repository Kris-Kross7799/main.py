from aiogram import Bot,Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api="8047255672:AAGCnrRCdzHz8SU9HYc9n40iVhLg17pFwvU"
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age=State()
    growth=State()
    weight=State()
    sex=State()

@dp.message_handler(commands=["start"])
async def all_message(message):
    await message.answer("Привет, я - бот, помогающий Твоему здоровью!\n"
                         "Для подсчёта суточной нормы калорий введите команду /Calories")

@dp.message_handler(commands=['Calories'])
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

@dp.message_handler()
async def start(message):
    await message.answer("Я - бот, помогающий твоему здоровью! Рад видеть Вас, "
                         "для начала нажмите /start")


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)