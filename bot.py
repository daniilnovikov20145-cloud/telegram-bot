import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8212324861:AAHGxT5eIKx1q6TRghBpSxe4TPX5PTxAF40"

GROUP_LINK = "https://t.me/+44ES5gKX_LAwYzNi"
WEBSITE_LINK = "https://insightorba.com/"
PERSONAL_LINK = "https://t.me/vekluch"

VACANCY_TEXT = """
Привіт , ми дуже раді що тебе зацікавила наша вакансія 🤝

Ми є великою американською компанією, яка працює вже понад 10 років в Америці та по всьому світу 😎

Наразі ми пропонуємо вакансію на один з наших проектів, який вже успішно працює понад 5 років та на якому працюють понад 450 співробітників 💪

Ми пропонуємо:

Формат роботи: дистанційно 💻
Графік: повна зайнятість — 8 годин на день, 5 днів на тиждень 📊
Напрям: підтримка, мотивація, спілкування з людьми 🙏

Що потрібно для роботи:
ПК / ноутбук + стабільний інтернет

Ми не є брачним агентством, онліком, вебками, офісами, скамом і тд ❌

Ми пропонуємо чесні умови, прозору бонусну систему, оплачуване навчання та багато інших переваг ✅

Якщо Вам це відгукується, ми запрошуємо Вас на Zoom конференцію у понеділок о 14:00 за Києвом 🤝

Під час конференції ми детально розповімо про компанію та відповімо на всі питання 🙋

Ось посилання на групу, де є вся інформація та буде доступ до зустрічі 👇
https://t.me/+44ES5gKX_LAwYzNi
"""

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Подати заявку на вакансію")],
        [
            KeyboardButton(text="ℹ️ Детальніше про вакансію"),
            KeyboardButton(text="🌐 Вебсайт"),
        ],
        [KeyboardButton(text="❓ Задати питання")],
    ],
    resize_keyboard=True
)

group_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👉 Перейти в групу", url=GROUP_LINK)]
    ]
)

website_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Відкрити вебсайт", url=WEBSITE_LINK)]
    ]
)

personal_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написати мені", url=PERSONAL_LINK)]
    ]
)

@dp.message(lambda message: message.text == "/start")
async def start(message: types.Message):
    await message.answer("Вітаємо в нашому боті 👋", reply_markup=main_kb)

@dp.message()
async def buttons(message: types.Message):
    if message.text == "📝 Подати заявку на вакансію":
        await message.answer(
            "Натисніть кнопку нижче щоб перейти в групу 🚀",
            reply_markup=group_kb
        )

    elif message.text == "ℹ️ Детальніше про вакансію":
        await message.answer(VACANCY_TEXT)

    elif message.text == "🌐 Вебсайт":
        await message.answer(
            "Натисніть кнопку нижче щоб перейти на сайт компанії 🌐",
            reply_markup=website_kb
        )

    elif message.text == "❓ Задати питання":
        await message.answer(
            "Натисніть кнопку нижче щоб написати мені в особисті повідомлення 💬",
            reply_markup=personal_kb
        )
@dp.message()
async def handle_unknown(message: types.Message):
    text = message.text

    if text in [
        "📩 Подати заявку на вакансію",
        "❓ Задати питання",
        "🌐 Вебсайт",
        "📄 Детальніше про вакансію"
    ]:  
        return

    await message.answer(
        "Я бачу, що у тебе є запитання 😊\n\n"
        "Щоб швидше знайти відповідь, обери, будь ласка, один із розділів нижче 👇\n\n"
        "Або напиши мені особисто 👉 @vekluch — я з радістю допоможу",
        reply_markup=main_kb
    )
async def main():
    await dp.start_polling(bot)

asyncio.run(main())
