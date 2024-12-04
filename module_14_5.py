from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from crud_functions import *

api = "8047255672:AAGCnrRCdzHz8SU9HYc9n40iVhLg17pFwvU"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="рассчитать"),
               KeyboardButton(text="информация")],
              [KeyboardButton(text="купить"),
               KeyboardButton(text="регистрация")]],
    resize_keyboard=True)

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Формулы рассчёта', callback_data='formulas'),
         InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')]])

ikb_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product_1', callback_data='product_buying'),
         InlineKeyboardButton(text='Product_2', callback_data='product_buying'),
         InlineKeyboardButton(text='Product_3', callback_data='product_buying'),
         InlineKeyboardButton(text='Product_4', callback_data='product_buying')]])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

class RegistrationState(StatesGroup):
    user_name = State()
    email = State()
    age = State()

@dp.message_handler(text='регистрация')
async def sigh_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.user_name.set()

@dp.message_handler(state=RegistrationState.user_name)
async def set_username(message, state):
    user_name = message.text
    if not is_included(user_name):
        await state.update_data(user_name=user_name)
        await message.answer("Введите свой email")
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')



@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    try:
        await state.update_data(age=int(message.text))
        data = await state.get_data()
        user_name = data['user_name']
        email = data['email']
        age = data['age']
        add_user(user_name, email, age)
        await message.answer("Регистрация прошла успешно!")
        await state.finish()
    except ValueError:
        await message.answer("Введите корректный возраст!")



# get_all_products()


@dp.message_handler(commands=["start"])
async def all_message(message):
    await message.answer("Привет, я - бот, помогающий Твоему здоровью!\n"
                         "Выберите опцию", reply_markup=kb)


@dp.callback_query_handler(text="formulas")
async def formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()  # команда, заверщающая вызов и делающая
    # кнопку снова активной


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer("ведите свой возраст")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(text=['рассчитать'])
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
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    sex = data['sex']
    if sex == 'м' or sex == "М" or sex == 'm' or sex == 'M':
        result = 10.0 * weight + 6.25 * growth - 5.0 * age + 5
    else:
        result = 10.0 * weight + 6.25 * growth - 5.0 * age - 161
    await message.answer(f"Ваша норма калорий {result} в день")
    await state.finish()


@dp.message_handler(text=["информация"])
async def info(message):
    await message.answer("Раздел в разработке...", reply_markup=kb)


@dp.message_handler(text=["купить"])
async def get_buying_list(message):
    products = get_all_products()
    for i in products:
        try:
            img_path = f'./({i[0]}).png'
            with open(img_path, 'rb') as img:
                await message.answer_photo(img, f'{i[1]}, {i[2]}, Цена: {i[3]}')
        except FileNotFoundError:
            await message.answer(f'No image. {i[1]}, {i[2]}, Цена: {i[3]}')
    await message.answer("выберите продукт для покупки:", reply_markup=ikb_2)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    # await call.answer()


@dp.message_handler()
async def start(message):
    await message.answer("Добро пожаловать! Рады видеть Вас, "
                         "для начала введите команду /start")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
