import time
import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
import text

TOKEN = "5738756421:AAGQXu9JWEmk_u3k2zs3WlsWJKW46VlGk7k"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

markup = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Потеря сознания", callback_data='mind')
item2 = types.InlineKeyboardButton("Наружные кровотечения", callback_data='blood')
item3 = types.InlineKeyboardButton("Инородные тела в дыхательных путях", callback_data='breath')
item4 = types.InlineKeyboardButton("Термическое воздействие", callback_data='temp')
item5 = types.InlineKeyboardButton("Поступление токсических веществ", callback_data='toxic')
item6 = types.InlineKeyboardButton("Поражение электрическим током", callback_data='shock')
item7 = types.InlineKeyboardButton("Укусы", callback_data='bite')
item8 = types.InlineKeyboardButton("Другое", callback_data='another')

markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_mame = message.from_user.full_name
    logging.info(f'{user_id=} {user_mame=} {time.asctime()}')
    mess = f'Привет, <b>{user_mame}</b>!\n\nЭтот telegram bot создан для того, чтобы помочь тебе узнать больше о первой помощи и чтобы ты смог правильно оказать её в том или ином случае.'
    # f' \n\nОт своевременности и качества оказания первой помощи в значительной степени зависит дальнейшее состояние здоровья пострадавшего и даже его жизнь. '
    # f'\nНо следует помнить, что первая помощь никогда не заменит квалифицированной медицинской помощи врача-специалиста, если в ней нуждается пострадавший.\n\nВведи нужный случай, при котором нужно оказать помощь!'

    await bot.send_message(user_id, mess, parse_mode='html', reply_markup=markup)

    for i in range(2000):
        time.sleep(60 * 60 * 24)
        # загружаем список фактов
        f = open('D:/FirstHelpBot/test/facts.txt', 'r', encoding='UTF-8')
        facts = f.read().split('\n')
        f.close()
        ans = random.choice(facts)
        await bot.send_message(user_id, ans)
#//////////////////////////////////////////////////////////////////////////////////////////////////

#ОБРАБОТКА КНОПКИ ПОТЕРЯ СОЗНАНИЯ
@dp.callback_query_handler(text='mind')
async def begin_mind(call: CallbackQuery):
    markup_mind = InlineKeyboardMarkup(row_width=1)
    item_m1 = types.InlineKeyboardButton("Дополнительно", callback_data='dop')
    markup_mind.add(item_m1)

    await call.message.answer( text.mind_text, parse_mode='html', reply_markup=markup_mind)

@dp.callback_query_handler(text='dop')
async def dop(call: CallbackQuery):
    await call.message.answer(text.cardioPulmonary_text, parse_mode='html')
#//////////////////////////////////////////////////////////////////////////////////////////////////

#ОБРАБОТКА КНОПКИ НАРУЖНЫЕ КРОВОТЕЧЕНИЯ
@dp.callback_query_handler(text='blood')
async def begin_blood(call: CallbackQuery):
    markup_blood = InlineKeyboardMarkup(row_width=1)
    item_b1 = types.InlineKeyboardButton("Как накладывать жгут?", callback_data='jgut')
    item_b2 = types.InlineKeyboardButton("Как проверить сознание пострадавшего?", callback_data='kakProverit')
    markup_blood.add(item_b1, item_b2)

    await call.message.answer(text.blood_text, parse_mode='html', reply_markup=markup_blood)

@dp.callback_query_handler(text='kakProverit')
async def have_mind(call: CallbackQuery):
    await call.message.answer(text.have_mind_text, parse_mode='html')

@dp.callback_query_handler(text='jgut')
async def jgut(call: CallbackQuery):
    markup_jgut = InlineKeyboardMarkup(row_width=1)
    item_j1 = types.InlineKeyboardButton("У вас нет жгута?", callback_data='not_jgut')
    markup_jgut.add(item_j1)
    await call.message.answer(text.jgut_text, parse_mode='html')
    await call.message.answer_photo('jgut.jpg', parse_mode='html')

@dp.callback_query_handler(text='not_jgut')
async def not_jgut(call: CallbackQuery):
    await call.message.answer(text.not_jgut_text, parse_mode='html')
    await call.message.answer_photo('not_jgut.jpg', parse_mode='html')
#//////////////////////////////////////////////////////////////////////////////////////////////////

#ОБРАБОТКА КНОПКИ Инородные тела в дыхательных путях
@dp.callback_query_handler(text='breath')
async def begin_breath(call: CallbackQuery):
    markup_breath = InlineKeyboardMarkup(row_width=1)
    item_bth1 = types.InlineKeyboardButton("У детей", callback_data='baby')
    item_bth2 = types.InlineKeyboardButton("У взрослых", callback_data='adult')
    markup_breath.add(item_bth1, item_bth2)
    await call.message.answer("<b>Инородные тела в верхних дыхательных путях</b>", parse_mode='html', reply_markup=markup_breath)

@dp.callback_query_handler(text='baby')
async def baby(call: CallbackQuery):
    await call.message.answer( text.baby_text, parse_mode='html')

@dp.callback_query_handler(text='adult')
async def adult(call: CallbackQuery):
    markup_adult = InlineKeyboardMarkup(row_width=1)
    item_alt1 = types.InlineKeyboardButton("Как проверить сознание пострадавшего?", callback_data='kakProverit')
    item_alt2 = types.InlineKeyboardButton("Последовательность проведения сердечно-легочной реанимации", callback_data=' dop')
    await call.message.answer( text.adult_text, parse_mode='html')
#//////////////////////////////////////////////////////////////////////////////////////////////////

#ОБРАБОТКА КНОПКИ Термическое воздействие
@dp.callback_query_handler(text='temp')
async def begin_temp(call: CallbackQuery):
    markup_temp = InlineKeyboardMarkup(row_width=1)
    item_tmp1 = types.InlineKeyboardButton("Ожоги", callback_data='burn')
    item_tmp2 = types.InlineKeyboardButton("Солнечный удар", callback_data='sunstroke')
    item_tmp3 = types.InlineKeyboardButton("Отморожение", callback_data='frostbite')
    item_tmp4 = types.InlineKeyboardButton("Общее переохлаждение", callback_data='hypothermia')
    markup_temp.add(item_tmp1, item_tmp2, item_tmp3, item_tmp4)
    await call.message.answer("<b>Термическое воздействие</b>", parse_mode='html', reply_markup=markup_temp)

@dp.callback_query_handler(text='burn')
async def burn(call: CallbackQuery):
    await call.message.answer(text.burn_text, parse_mode='html')


@dp.callback_query_handler(text='sunstroke')
async def sunstroke(call: CallbackQuery):
    markup_sunstroke = InlineKeyboardMarkup(row_width=1)
    item_snstrk = types.InlineKeyboardButton("Последовательность проведения сердечно-легочной реанимации", callback_data='dop')
    await call.message.answer(text.sunstroke_text, parse_mode='html', reply_markup=markup_sunstroke)

@dp.callback_query_handler(text='frostbite')
async def frostbite(call: CallbackQuery):
    await call.message.answer(text.frostbite_text, parse_mode='html')

@dp.callback_query_handler(text='hypothermia')
async def hypothermia(call: CallbackQuery):
    await call.message.answer(text.hypothermia_text, parse_mode='html')
#//////////////////////////////////////////////////////////////////////////////////////////////////

#ОБРАБОТКА КНОПКИ Поступление токсических веществ
@dp.callback_query_handler(text='toxic')
async def begin_toxic(call: CallbackQuery):
    markup_toxic = InlineKeyboardMarkup(row_width=1)
    item_txc1 = types.InlineKeyboardButton("<b>Первая помощь при поступлении токсического вещества через рот</b>", callback_data='toxic_mounth')
    item_txc2 = types.InlineKeyboardButton("<b>Первая помощь при поступлении токсического вещества через дыхательные пути</b>", callback_data='toxic_breath')
    markup_toxic.add(item_txc1, item_txc2)
    await call.message.answer("<b>Поступление токсических веществ</b>", parse_mode='html', reply_markup=markup_toxic)

@dp.callback_query_handler(text='toxic_mounth')
async def toxic_mounth(call: CallbackQuery):
    markup_toxic_mounth = InlineKeyboardMarkup(row_width=1)
    item_txc_mnth = types.InlineKeyboardButton("Последовательность проведения сердечно-легочной реанимации", callback_data='dop')
    markup_toxic_mounth.add(item_txc_mnth)
    await call.message.answer(text.toxic_mounth_text, parse_mode='html')

@dp.callback_query_handler(text='toxic_breath')
async def toxic_breath(call: CallbackQuery):
    markup_toxic_breath = InlineKeyboardMarkup(row_width=1)
    item_txc_brth = types.InlineKeyboardButton("Последовательность проведения сердечно-легочной реанимации", callback_data='dop')
    markup_toxic_breath.add(item_txc_brth)
    await call.message.answer(text.toxic_breath_text, parse_mode='html')
#//////////////////////////////////////////////////////////////////////////////////////////////////

#ОБРАБОТКА КНОПКИ Поражение электрическим током
@dp.callback_query_handler(text='shock')
async def begin_shock(call: CallbackQuery):
    markup_shock = InlineKeyboardMarkup(row_width=1)
    item_shck1 = types.InlineKeyboardButton("Последовательность проведения сердечно-легочной реанимации", callback_data='dop')
    markup_toxic.add(item_shck1)
    await call.message.answer(text.shock_text, parse_mode='html', reply_markup=markup_shock)
#//////////////////////////////////////////////////////////////////////////////////////////////////
#ОБРАБОТКА КНОПКИ УКУСЫ
@dp.callback_query_handler(text='bite')
async def begin_bite(call: CallbackQuery):
    markup_bite = InlineKeyboardMarkup(row_width=1)
    item_1 = types.InlineKeyboardButton("Укусы ядовитых змей", callback_data='sneak')
    item_2 = types.InlineKeyboardButton("Укусы насекомых", callback_data='insect')
    markup_bite.add(item_1, item_2)

    await call.message.answer('Укусы:', parse_mode='html', reply_markup=markup_bite)
@dp.callback_query_handler(text='sneak')
async def sneak(call: CallbackQuery):
    await call.message.answer(text.sneak_text, parse_mode='html')
@dp.callback_query_handler(text='insect')
async def sneak(call: CallbackQuery):
    await call.message.answer(text.insect_text, parse_mode='html')
#//////////////////////////////////////////////////////////////////////////////////////////////////

#ОБРАБОТКА КНОПКИ ДРУГОЕ
@dp.callback_query_handler(text='another')
async def begin_another(call: CallbackQuery):
    markup_another = InlineKeyboardMarkup(row_width=1)
    item_a1 = types.InlineKeyboardButton("Оптимальное положение тела в зависимости от случая", callback_data='position')
    item_a2 = types.InlineKeyboardButton("Извлечение пострадавшего из автомобиля или труднодоступного места", callback_data='extraction')
    item_a3 = types.InlineKeyboardButton("Транспортировка пострадавших", callback_data='transportation')
    markup_another.add(item_a1, item_a2, item_a3)

    await call.message.answer("<b>Другое</b>", parse_mode='html')

@dp.callback_query_handler(text='position')
async def position(call: CallbackQuery):
    await call.message.answer(text.position_text, parse_mode='html')

@dp.callback_query_handler(text='extraction')
async def extraction(call: CallbackQuery):
    await call.message.answer(text.extraction_text, parse_mode='html')
    await call.message.answer_photo('extraction1.jpg', parse_mode='html')
    await call.message.answer_photo('extraction2.jpg', parse_mode='html')

@dp.callback_query_handler(text='transportation')
async def transportation(call: CallbackQuery):
    await call.message.answer(text.transportation_text, parse_mode='html')
    await call.message.answer_photo('перенос1.jpg', parse_mode='html')
    await call.message.answer_photo('перенос2.jpg', parse_mode='html')
#//////////////////////////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    executor.start_polling(dp)
