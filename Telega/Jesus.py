from TOKEN import TOKEN, PayTOKEN
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
import asyncio
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultGame
loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dis = Dispatcher(bot, loop=loop)
# Коллекция музыки
dismis = ["Слава Сатане", "Мудак", "Козёл", "Сука", "мудак", "козёл", "сука"]
f = ["E:/Projects/Python/projects/Telega/music/Get.mp3", "E:/Projects/Python/projects/Telega/music/Eric - Poker Face.mp3",
     "E:/Projects/Python/projects/Telega/music/Game of Thrones.mp3", "E:/Projects/Python/projects/Telega/music/Salty Balls - Chef.mp3"]
# Кнопка музыки и приветствия
musbutton = KeyboardButton("Музыка")
button = KeyboardButton("Привет")
geo = KeyboardButton("Geolocation", request_location=True)
sc = ReplyKeyboardMarkup(resize_keyboard=True)#can use , one_time_keyboard=True для того чтобы спрятать клаву
sc.row(button, geo)
sc.row(musbutton)
# Инлайн кнопки
what = InlineKeyboardButton("Дурак что ли ?", callback_data="durak")
sry = InlineKeyboardButton("Прости не правельно написал(а)", callback_data="sry")
ikm = InlineKeyboardMarkup()
ikm.row(what, sry)
# Кнопка Доната
donat = KeyboardButton("Дать денежку")
price = types.LabeledPrice(label="Дать денежку боту", amount=6000)
sc.row(donat)
# Донат
@dis.pre_checkout_query_handler(lambda query: True)
async def answer_payment(checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(checkout_query.id, ok=True)
@dis.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
async def successful(message: types.Message):
    await bot.send_message(message.from_user.id, f"Денежки пришли {message.successful_payment.total_amount // 100}{message.successful_payment.currency}"
                                                 f", спасибо тебе\nИисус любит тебя")
    f = open("E:\Pictures\\avatar\jesus.jpg", 'rb')
    await bot.send_photo(message.chat.id, f)
# Коллбеки для инлайн кнопок
@dis.callback_query_handler(lambda c : c.data == "durak")
async def durak(callback : types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, "Еслы бы я написал это сообщение в двоичном коде, ты бы тоже ничего не понял")

@dis.callback_query_handler(lambda c : c.data == "sry")
async def sry(callback : types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, "Ничего страшного, напиши ещё раз своё сообщение")


#/start приветствие

@dis.message_handler(commands=["start"])
async def process(message=types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAEBqqBf0M-lRxXc9y9IrALGix8o_17ZNgACogYAAmMr4gnSxdCG4azufB4E", reply_markup=sc)
    await bot.send_message(message.from_user.id, "Привет, ты вернулся?" + "\nНапиши чем ты обеспокоен")
#Помощь

@dis.message_handler(commands=["help"])
async def helping(message=types.Message):
    await message.reply("/start\nзапустить бота (Заставить Иисуса работать.)")

# Общение
@dis.message_handler()
async def talk(message=types.Message):
    if message.text == 'Дать денежку':
        if PayTOKEN.split(":")[1] == "TEST":
            await bot.send_invoice(
                message.chat.id,
                title="Пожертвование",  # Заголовок
                description="Вы даёте денежку боту для того, чтобы он развивался.",  # Описание товара
                provider_token=PayTOKEN,  # провайдер токен
                currency='RUB',  # курс
                photo_url='https://www.hopeservices.org/wp-content/uploads/SEC-HERO-donations.jpg',  # Ссылка но фото
                photo_width=400,  # Ширина, пиши вместо размера !=0/None тогда картинка не появится
                photo_height=300,  # Высота
                # здесь может быть size если картинка квадратная
                is_flexible=False,  # True если конечная цена зависит от способа доставки
                prices=[price],  # название списка с ценами(на данный момент она одна)
                start_parameter="Donation",  # стартовый параметр
                payload="Loading"  # Не показывается пользователю, но после успешной оплаты можно (мне) посмотреть
            )
    if message.text == "Музыка":
        ranusic = open(random.choice(f), "rb")
        await bot.send_audio(message.from_user.id, ranusic)
    if message.text == "Привет":
        await message.answer_sticker("CAACAgIAAxkBAAEBqsFf0QGyiN7S2QjaHpSXTGsAAefaB7YAArEEAALyfoIMWnVLOfcTAUweBA")
        await bot.send_message(message.from_user.id, "Привет "+message.from_user.first_name)
    if message.text in dismis:
        await message.answer_sticker("CAACAgIAAxkBAAEBsT5f3NkqfVfJasAwlOU3oP9HAha6ggACBQEAAladvQq35P22DkVfdx4E")
        await bot.send_message(message.from_user.id, "Пошёл отсюда ЕРЕТИК")
    elif message.text != "Музыка" and message.text != "Привет" and message.text != "Geolocation" and message.text != 'Дать денежку':
        await message.answer_sticker("CAACAgIAAxkBAAEBsUJf3N92IKYfkDWDcJbVneSac3iQSgAC4gcAApb6EgUg_e_RXphX5x4E")
        await bot.send_message(message.from_user.id, "Что? я тебя не понимаю", reply_markup=ikm)

if __name__ == "__main__":
    executor.start_polling(dis)