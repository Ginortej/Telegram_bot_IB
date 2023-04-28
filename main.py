import telebot # импортируем все нужные библеотеки
from tok import *
import asyncio
from telebot import types
from parsing import Parsing

bot = telebot.TeleBot(TOCKIN) #прописываем токен боту с которым он будет связан 

# прописываем все ссылки на ресурсы от куда будем брать информацию (ссфлки могут устаривать по этому они записаны как отдельные перменный для того что бы можно было в любой момент изменить)
official_site_topowasp = 'https://owasp.org/www-project-top-ten/'
official_site_attacks = 'https://www.vedomosti.ru/technology/news/2023/01/19/959680-okolo-50-0000-kiberatak-otrazili-v-rossii-za-proshlii-god'
official_site_ib = 'https://news.microsoft.com/ru-ru/features/protect-yourself-online/'

result_answer_true = 0 #счетчик правельных ответов
result_answer_false = 0 #счетчик не правильных ответов 

#start
@bot.message_handler(commands=['start'])
def button_message(message):
    #создем клвиатуру 
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    # создаем кнопки
    item1 =types.KeyboardButton("Топ-10 OWASP") 
    item2 = types.KeyboardButton("Кол-во атак")
    item3 = types.KeyboardButton("Как себя обезопасить?")
    item4 = types.KeyboardButton("Тест на инфамоционую грамотность")
    markup.add(item1, item2, item3, item4) # добаляем их в уже созданую клавиатуру 
    bot.send_message(message.chat.id,'Привет я помогу тебе узнать чуть больше о информационой безопастности и улучшить свою безопастность',reply_markup=markup) # выводим в чат приветсвие и выводим клавиатуру
    print(message.chat.first_name) # пичает  вконосоль  всех кто ввел команду /start бота то есть запустил его

# action
@bot.message_handler(content_types=['text'])
def func_text(message):
    # прописываем последстиве на нажатые кнопки 
    if message.text == "Топ-10 OWASP": # пишем сдесь что если в чате от пользователя есть такое сообщение то выполнять следующие действия 
       info_pars_top10owasp = Parsing(url = official_site_topowasp, driver= '/geckodriver.exe') # Инцулизируем класс парсинга вставляем конкретный сайт и ссылку на драйвер брузера
       result_pars_top10owasp = [info_pars_top10owasp.paht_x(f'/html/body/main/div/div[1]/section[1]/ul/li[{i}]') for i in range(1,11)]# создаем генератор и пребераем от 1 до 11 и подстовляем значение в путь до нашего тега
       bot.send_message(message.chat.id, '\n—'.join(result_pars_top10owasp)) # далее одним сообщением спомощю метода join запускаем генератор и с новой строки выводим наши теги(join тут нужен что бы запустить гениратор и выводимые значения тегов не были в типе данных списков)
       info_pars_top10owasp.clous()#Так как парскер парсит данные через веб драйвер для того что бы наш сервер не могли задудосить мы его закрываем 
       bot.send_message(message.chat.id,f"офийальный сайт {official_site_topowasp}") # даем ссылку на ресурс от куда брали информацию
    # прописываем последстиве на нажатые кнопки 
    
    elif message.text == "Кол-во атак":# пишем сдесь что если в чате от пользователя есть такое сообщение то выполнять следующие действия 
        info_pars = Parsing(url = official_site_attacks, driver= '/geckodriver.exe')# Инцулизируем класс парсинга вставляем конкретный сайт и ссылку на драйвер брузера
        bot.send_message(message.chat.id,info_pars.paht_x('/html/body/div/div[2]/div/div[2]/div[3]/div/article[1]/div[1]/div/div/div/div[1]/div[1]/div/p')) # выводим только один тег который нам понадобиться и выводим его в чат
        bot.send_message(message.chat.id,f"офийальный сайт {official_site_attacks}") # даем ссылку на ресурс от куда брали информацию
        info_pars.clous()# Так как парскер парсит данные через веб драйвер для того что бы наш сервер не могли задудосить мы его закрываем 
    # прописываем последстиве на нажатые кнопки 
    
    elif message.text == "Как себя обезопасить?":# пишем сдесь что если в чате от пользователя есть такое сообщение то выполнять следующие действия 
        info_pars_ib = Parsing(url = official_site_ib, driver= '/geckodriver.exe')# Инцулизируем класс парсинга вставляем конкретный сайт и ссылку на драйвер брузера
        teg_pars_ib = ['3','5','8','10','11', '14','17','19']
        result_pars_ib_teg_p = [info_pars_ib.paht_x(f'/html/body/div[3]/div/main/div[1]/section[1]/div/p[{i}]') for i in teg_pars_ib] #
        bot.send_message(message.chat.id, '\n—'.join(result_pars_ib_teg_p))# далее одним сообщением спомощю метода join запускаем генератор и с новой строки выводим наши теги
        bot.send_message(message.chat.id,f"офийальный сайт {official_site_ib}")# даем ссылку на ресурс от куда брали информацию
        info_pars_ib.clous()#Так как парскер парсит данные через веб драйвер для того что бы наш сервер не могли задудосить мы его закрываем 
    # прописываем последстиве на нажатые кнопки

    elif message.text == "Тест на инфамоционую грамотность":# пишем сдесь что если в чате от пользователя есть такое сообщение то выполнять следующие действия
        markup_2 = types.InlineKeyboardMarkup() # Создаем клавиатуру
        button1 = types.InlineKeyboardButton(text= 'Готов', callback_data= 'start_test')# создаем кнопки
        button2 = types.InlineKeyboardButton(text='Пока не готов', callback_data= 'clous_test')# создаем кнопки
        markup_2.add(button1, button2) # добаляем их в уже созданую клавиатуру 
        bot.send_message(message.chat.id,'Нажми готов если хочешь начать тест',reply_markup=markup_2) # выводим в чат приветсвие и выводим клавиатуру
        

    @bot.callback_query_handler(func=lambda call:True)
    def callback_query(call):# прописываем последстиве на нажатые кнопки
        global result_answer_true # ипортариуем глобальные переменные
        global result_answer_false # ипортариуем глобальные переменные
        if call.data == 'clous_test':# пишем здесь что если пользователь нажал конкретную кнопку за которым закрепленны данные обратного вызова то выполнять следующие действия
            bot.delete_message(call.message.chat.id, call.message.message_id)# сздесь мы удаляем клавиатуру так как данное действие подкрпленно к нопки "Пока не готов"
        # elif call.data == 'error_start':# пишем здесь что если пользователь нажал конкретную кнопку за которым закрепленны данные обратного вызова то выполнять следующие действия. Данное условие созданно что бы записывать ошибки сделанные при ответе теста
        #     if call.data == 'error_start':
        #         print('sdasd')
            # result_answer_false = result_answer_false + 1# добавляем перемменой +1 так как это наш счетчик 
            # result_answer_true = result_answer_true - 1# Убираем -1 из нашего счетчика 
            # markup_test_1 = types.InlineKeyboardMarkup()# Создаем клавиатуру
            # markup_test_1.add(types.InlineKeyboardButton(text='1', callback_data= 'error_start'), types.InlineKeyboardButton(text='2', callback_data= 'error_start'), types.InlineKeyboardButton(text='3', callback_data= 'result_1'), types.InlineKeyboardButton(text='4', callback_data= 'error_start'))# добаляем конпки и сразу же в этой функции их создаем
            # bot.edit_message_text('Попробуй еще раз\n1:password1234        2:Link2003\n3:Gezeru2n4Nes!we5      4:BICE', reply_markup= markup_test_1 , chat_id=call.message.chat.id, message_id=call.message.message_id)# Данная функциия изменят последние сообщение нашего бота а то есть клавиатуру 
        elif call.data == 'start_test' or call.data == 'error_start':# пишем здесь что если пользователь нажал конкретную кнопку за которым закрепленны данные обратного вызова то выполнять следующие действия.
            if call.data == 'error_start':
                result_answer_false = result_answer_false + 1# добавляем перемменой +1 так как это наш счетчик 
                result_answer_true = result_answer_true - 1# Убираем -1 из нашего счетчика
                markup_test_1 = types.InlineKeyboardMarkup()# Создаем клавиатуру
                markup_test_1.add(types.InlineKeyboardButton(text='1', callback_data= 'error_start'), types.InlineKeyboardButton(text='2', callback_data= 'error_start'), types.InlineKeyboardButton(text='3', callback_data= 'result_1'), types.InlineKeyboardButton(text='4', callback_data= 'error_start'))# добаляем конпки и сразу же в этой функции их создаем
                bot.edit_message_text('Попробуй еще раз\n1:password1234        2:Link2003\n3:Gezeru2n4Nes!we5      4:BICE', reply_markup= markup_test_1 , chat_id=call.message.chat.id, message_id=call.message.message_id)# Данная функциия изменят последние сообщение нашего бота а то есть клавиатуру 
            elif call.data == 'start_test':
                markup_test_1 = types.InlineKeyboardMarkup() # Создаем клавиатуру 
                markup_test_1.add(types.InlineKeyboardButton(text='1', callback_data= 'error_start'), types.InlineKeyboardButton(text='2', callback_data= 'error_start'), types.InlineKeyboardButton(text='3', callback_data= 'result_1'), types.InlineKeyboardButton(text='4', callback_data= 'error_start')) # добаляем конпки и сразу же в этой функции их создаем
                bot.edit_message_text('Тогда начнем\nПервый впорос какой из поролей более безопастней?\n1:password1234        2:Link2003\n3:Gezeru2n4Nes!we5      4:BICE', reply_markup= markup_test_1 , chat_id=call.message.chat.id, message_id=call.message.message_id)# Данная функциия изменят последние сообщение нашего бота а то есть клавиатуру  

        elif call.data == 'error_1':# пишем здесь что если пользователь нажал конкретную кнопку за которым закрепленны данные обратного вызова то выполнять следующие действия. 
            result_answer_false = result_answer_false + 1# добавляем перемменой +1 так как это наш счетчик 
            result_answer_true = result_answer_true - 1# Убираем -1 из нашего счетчика 
            markup_test_2 = types.InlineKeyboardMarkup()# Создаем клавиатуру 
            markup_test_2.add(types.InlineKeyboardButton(text='Нет', callback_data= 'result_2'), types.InlineKeyboardButton(text='Да', callback_data= 'error_1')) #добаляем конпки и сразу же в этой функции их создаем
            bot.edit_message_text('Попробую еще раз это не правильно\nДавай теперь загрыаем не большую ситуацию тебе в телегрм или вк пришло сообщение от незнакомого человека в письме было то что перейдя по ссылки ты получишь к примеру 1000 рублей\nПерейдешь ты по ссылки проверя правд это или нет ?', reply_markup= markup_test_2 , chat_id=call.message.chat.id, message_id=call.message.message_id)# Данная функциия изменят последние сообщение нашего бота а то есть клавиатуру  
        elif call.data == 'result_1':#пишем здесь что если пользователь нажал конкретную кнопку за которым закрепленны данные обратного вызова то выполнять следующие действия.
            result_answer_true = result_answer_true + 1# обавляем перемменой +1 так как это наш счетчик 
            markup_test_2 = types.InlineKeyboardMarkup()# Создаем клавиатуру  
            markup_test_2.add(types.InlineKeyboardButton(text='Нет', callback_data= 'result_2'), types.InlineKeyboardButton(text='Да', callback_data= 'error_1')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Давай теперь загрыаем не большую ситуацию тебе в телегрм или вк пришло сообщение от незнакомого человека в письме было то что перейдя по ссылки ты получишь к примеру 1000 рублей\nПерейдешь ты по ссылки проверя правд это или нет ?', reply_markup= markup_test_2 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'error_2':#
            result_answer_false = result_answer_false + 1#
            result_answer_true = result_answer_true - 1#
            markup_test_3 = types.InlineKeyboardMarkup()#
            markup_test_3.add(types.InlineKeyboardButton(text='1', callback_data= 'result_3'), types.InlineKeyboardButton(text='2', callback_data= 'error_2')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Давай теперь рассмотрим следующию ситуацию к примеру ты зашел в кафе вкусно и точка\nТы взял заказ сел кушать но тут тебе захотелось посмотреть тик ток или полазить еще в каких то соцсетях\nно совсем забыл заплатить за интернет и вскоре решил подключиться к сети вкусно и точка\nподклюившись ты видишь выскакивающий банер о том что нужно зарегестрироваться\nТвои действия?\n1: Спрошу есть ли вообще в уафе бесплтаный фай вай и нужно ли там регистрироваться\n2: Зарегестриуюсь что тут того', reply_markup= markup_test_3 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'result_2':#
            result_answer_true = result_answer_true + 1#
            markup_test_3 = types.InlineKeyboardMarkup()#
            markup_test_3.add(types.InlineKeyboardButton(text='1', callback_data= 'result_3'), types.InlineKeyboardButton(text='2', callback_data= 'error_2')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Давай теперь рассмотрим следующию ситуацию к примеру ты зашел в кафе вкусно и точка\nТы взял заказ сел кушать но тут тебе захотелось посмотреть тик ток или полазить еще в каких то соцсетях\nно совсем забыл заплатить за интернет и вскоре решил подключиться к сети вкусно и точка\nподклюившись ты видишь выскакивающий банер о том что нужно зарегестрироваться\nТвои действия?\n1: Спрошу есть ли вообще в уафе бесплтаный фай вай и нужно ли там регистрироваться\n2: Зарегестриуюсь что тут того', reply_markup= markup_test_3 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'error_3':#
            result_answer_false = result_answer_false + 1#
            result_answer_true = result_answer_true - 1#
            markup_test_3 = types.InlineKeyboardMarkup()#
            markup_test_3.add(types.InlineKeyboardButton(text='1', callback_data= 'error_3'), types.InlineKeyboardButton(text='2', callback_data= 'result_4'), types.InlineKeyboardButton(text='3', callback_data= 'result_4')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Давай теперь преположим что ты замеаешь что в твоей соц сети к примеру в вк кто пишет от твоего лица разным людям\nКак ты поступишь в такой ситуации\n1: Начну писать что это не я\n2: Посмотрю какие устройства заходили на мою страницу и закончу все сеансы после чего сменю пороль\n3: Буду просить деньги а потом все это скину на взлом АХАХАХ', reply_markup= markup_test_3 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'result_3':#
            result_answer_true = result_answer_true + 1#
            markup_test_3 = types.InlineKeyboardMarkup()#
            markup_test_3.add(types.InlineKeyboardButton(text='1', callback_data= 'error_3'), types.InlineKeyboardButton(text='2', callback_data= 'result_4'), types.InlineKeyboardButton(text='3', callback_data= 'result_4')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Давай теперь преположим что ты замеаешь что в твоей соц сети к примеру в вк кто пишет от твоего лица разным людям\nКак ты поступишь в такой ситуации\n1: Начну писать что это не я\n2: Посмотрю какие устройства заходили на мою страницу и закончу все сеансы после чего сменю пороль\n3: Буду просить деньги а потом все это скину на взлом АХАХАХ', reply_markup= markup_test_3 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'error_4':#
            result_answer_false = result_answer_false + 1#
            result_answer_true = result_answer_true - 1#
            markup_test_4 = types.InlineKeyboardMarkup()#
            markup_test_4.add(types.InlineKeyboardButton(text='1', callback_data= 'error_4'), types.InlineKeyboardButton(text='2', callback_data= 'result_5'), types.InlineKeyboardButton(text='3', callback_data= 'result_5')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Рассмотрим следующию ситуацию у тебя украли аккаунт какой то из соц сетей к примеру Инстограмм\nТвои действия?\n1: Создам новый аккаунт      2: Попытаюсь востонновить аккаунт всеми возможными спосабами\n3: Напиши в поддержку о помощи', reply_markup= markup_test_4 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'result_4':#
            result_answer_true = result_answer_true + 1#
            markup_test_4 = types.InlineKeyboardMarkup()#
            markup_test_4.add(types.InlineKeyboardButton(text='1', callback_data= 'error_4'), types.InlineKeyboardButton(text='2', callback_data= 'result_5'), types.InlineKeyboardButton(text='3', callback_data= 'result_5')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Рассмотрим следующию ситуацию у тебя украли аккаунт какой то из соц сетей к примеру Инстограмм\nТвои действия?\n1: Создам новый аккаунт      2: Попытаюсь востонновить аккаунт всеми возможными спосабами\n3: Напиши в поддержку о помощи', reply_markup= markup_test_4 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'error_5':#
            result_answer_false = result_answer_false + 1#
            result_answer_true = result_answer_true - 1#
            markup_test_4 = types.InlineKeyboardMarkup()#
            markup_test_4.add(types.InlineKeyboardButton(text='Продолжу играть тут ничего нет того', callback_data= 'error_5'), types.InlineKeyboardButton(text='Удалю игру и аккаут в этой игре', callback_data= 'result_end'), types.InlineKeyboardButton(text='Установлю пиратку в которой будет вырезанно подключение к сети что бы мои данные не могли больше не куда передоваться', callback_data= 'result_end')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Попробую еще раз это не правильно\nНу вот и последний вопрос\nТы решил\а скачать к примеру игру майнкрафт\nно после установки ты увидл\а новость о том что компания которая создала эту игру брала твои данные и продовала рекламщикам что бы впехнуть тебе побольше рекламы\nтвои действия?', reply_markup= markup_test_4 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'result_5':#
            result_answer_true = result_answer_true + 1#
            markup_test_4 = types.InlineKeyboardMarkup()#
            markup_test_4.add(types.InlineKeyboardButton(text='1', callback_data= 'error_5'), types.InlineKeyboardButton(text='2', callback_data= 'result_end'), types.InlineKeyboardButton(text='3', callback_data= 'result_end')) # добаляем их в уже созданую клавиатуру 
            bot.edit_message_text('Ну вот и последний вопрос\nТы решил\а скачать к примеру игру майнкрафт\nно после установки ты увидл\а новость о том что компания которая создала эту игру брала твои данные и продовала рекламщикам что бы впехнуть тебе побольше рекламы\nтвои действия?\n1: Продолжу играть тут ничего нет того\n2: Удалю игру и аккаут в этой игре\n3: Установлю пиратку в которой будет вырезанно подключение к сети что бы мои данные не могли больше не куда передоваться', reply_markup= markup_test_4 , chat_id=call.message.chat.id, message_id=call.message.message_id)#
        elif call.data == 'result_end':# пишем здесь что если пользователь нажал конкретную кнопку за которым закрепленны данные обратного вызова то выполнять следующие действия.
            bot.delete_message(call.message.chat.id, call.message.message_id)# Удаляем нашу клавиатуру 
            if result_answer_true >= 3: # проверям счетчик через условие
                bot.send_message(message.chat.id,f'Ты молодец!!\nвот твой результат\nправельных ответов:{result_answer_true}\nне правилиных ответов:{result_answer_false}')# если условие верно то выводим то что пользовотель молодец и его результат
            elif result_answer_true < 3:# проверям счетчик через условие
                bot.send_message(message.chat.id,f'Эх почитай еще раз как себя обезопасить друг\nвот твой результат\nправельных ответов:{result_answer_true}\nне правилиных ответов:{result_answer_false}')# если условие верно то выводим то что пользовотель не совсем молодец и его результат

bot.infinity_polling()# запуск бота по средствам дикоратора
