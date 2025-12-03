from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from button import reply_kb, inline_kb_buy, inline_kb_more, inline_kb_sbp
from datetime import date, time, datetime
from utils import months
import asyncio
from urllib.parse import quote
import json


bot = Bot(token="8128703481:AAFR8BvV_0beNsHE__NXHbsd9k_aCCDvWlc")
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Выберите действие.",
        reply_markup=reply_kb
    )

@dp.message(Command("add"))
async def buy_free_ticket(message: Message):
    year = str(date.today()).split("-")[0]
    month = months[str(date.today()).split("-")[1]]
    day = str(date.today()).split("-")[2]
    date_buy = quote(f"{day} {month} {year} г.")
    now = datetime.now()
    time_buy = quote(f"{now.hour}:{now.minute}")
    args = message.text.split()[1:]

    if len(args) != 2:
        await message.answer("Использование: /add [номер маршрута] [номер автобуса]")
        return

    arg1, arg2 = args

    builder = ReplyKeyboardBuilder()

    # Создаем кнопку с Web App
    builder.button(
        text="Открыть мини-приложение",
        web_app=WebAppInfo(url=f"https://bababoy388.github.io/ticket/?arg1={arg1}&arg2={arg2}&date_buy={date_buy}&time_buy={time_buy}")
    )

    builder.adjust(1)

    await message.answer(
        "Нажми кнопку ниже чтобы открыть приложение",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )


@dp.message(F.web_app_data)
async def handle_web_app_data(message: Message):
    # Получаем данные из мини-приложения
    try:
        data = json.loads(message.web_app_data.data)
        user_id = data.get('user_id')
        text = data.get('message')

        await message.answer(
            f"Получены данные от Web App:\n"
            f"User ID: {user_id}\n"
            f"Message: {text}"
        )
    except Exception as e:
        await message.answer(f"Ошибка обработки данных: {e}")

# ================== Обработка кнопок ==================

@dp.message((F.text == "Купить билет"))
async def buy_ticket(message: Message):
    await message.answer("Способ покупки:",
                         reply_markup=inline_kb_buy)

@dp.message((F.text == "Действующие билеты"))
async def buy_ticket(message: Message):
    await message.answer("Действующих билетов нет.")

@dp.message((F.text == "Подписка СБП"))
async def buy_ticket(message: Message):
    await message.answer("Подписок нет.",
                         reply_markup=inline_kb_sbp)

@dp.message((F.text == "Ещё..."))
async def buy_ticket(message: Message):
    await message.answer("Выберите действие из списка.",
                         reply_markup=inline_kb_more)

# ======================================================


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())