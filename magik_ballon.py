import random
import time

antwort_schreib = ['Напиши свой вопрос что бы ответ был в формате Да или Нет', 'спрашивай...', 'говори давай...', 'я думал чуток отдохнуть...пиши давай свой вопрос',
            'ну давай, изрыгай..... ой извергай свои фантастически интересные вопросы', 'не томи... мне на горшок надо, пиши вопрос',
            'я надеялся, что больше тебя не увижу, давай пиши', 'умные люди книжки читают, а ты ..... пиши вопрос',
            'не ну ты давай, как-нибудь определяйся.... с вопросом. Знаешь, где клавиатура? набирай вопрос',
            'Давай, не стесняйся, пиши свой вопрос', 'Ну что, готов задать свой вопрос или еще колеблешься?',
            'Не теряй время, пиши свой вопрос прямо сейчас', 'Знаешь, я уже соскучился по твоим вопросам, давай не заставляй меня ждать',
            'Ты здесь, чтобы задавать вопросы, а не промедлять. Пиши!', 'Пиши свой вопрос, я с нетерпением жду твоей любопытной мысли',
            'У тебя есть возможность получить ответ на свой вопрос. Не упускай ее!',
            'Твои вопросы интересны для меня. Пиши без стеснения', 'Напиши свой вопрос и дай мне возможность помочь тебе']

antwort_allein1 = ['интересный вопрос, сейчас посмотрю в картах', 'а что - нибудь по легче?', 'я кофейную гущу разлил, ничего не вижу',
            'может такое у себя сам спросишь?', 'а нормальные вопросы закончились?', 'ты дествительно хочешь знать ответ?',
            'я был о тебе лучшего мнения....', 'Ах, интересный вопрос! Дай-ка я сначала проверю свои гадалки.', 'А что, не хватает сложностей? Может, я позвоню экстрасенсам?',
            'Ох, кофейная гуща... Интересное решение для просмотра вопросов.', 'Ну да, ну да. Может, действительно стоит спросить самого себя?',
            'Ой, прости, у меня кончились нормальные ответы. Может, ты поделишься парой?',
            'Конечно, я настолько любопытен, что не могу пропустить ни один вопрос!', 'Ого, я был так готов к твоему вопросу. Жаль, что оказался разочарован...',
            'Ну, кто бы мог подумать, что ты меня разочаруешь...', 'А, я понял. Тебе нужен ответ от источника высшей интеллектуальной мудрости, не так ли?',
            'Прекрасно! Ты прямо та самая умная и особенная персона, чье мнение мне так важно.',
            'Ну, мне о тебе говорили одни комплименты, но теперь я начинаю сомневаться...', 'Ого, почему я не догадался, что ты хочешь задать вопрос? Возможно, потому что это было слишком очевидно.',
            'Ты точно уверен, что хочешь знать ответ? Это может изменить всю твою жизнь, предупреждаю!',
            'Ах, я думал, ты здесь, чтобы задавать глупые вопросы. Как приятно ошибаться!', 'Не могу себя удержать от сарказма. Твой вопрос очень важен для меня, я плачу от счастья.']

antwort_allein2 =  [ 'я кофейную гущу разлил, ничего не вижу', 'может такое у себя сам спросишь?', 'а нормальные вопросы закончились?', 'ты действительно хочешь знать ответ?',
            'я был о тебе лучшего мнения....', 'в картах ничего нет... сейчас почитаю звезды', 'хз...хз... хз... может лучше фильм посмотрим?',
            'знаю, не знаю, я думал, что я умнее...', 'не вижу.... но посмотрю', 'может тебе чужой ответ подсунуть',
            'ответы, ответ, ответы.... где-то я записывал', 'как у этой персоны вообще оказался компьютер в руках?', 'ну давай, ответь сам на свой вопрос',
            'какое важное дело, что сразу ответ нужен?', 'давай сначала соберем все данные, а потом я решу, стоит ли отвечать',
            'твой вопрос такой оригинальный, что я сам не знаю, что ответить', 'ты спрашиваешь, как будто я магический шар',
            'прости, я сейчас занят перевариванием своего последнего вопроса', 'ответить на этот вопрос стоит целого года обдумывания',
            'у меня есть два варианта: "да" или "может быть". Какой выберешь?', 'если бы я знал ответ, то уже давно стал бы миллионером',
            'может лучше спросим у соседа?', 'хороший вопрос. Но я думаю, что ты сам знаешь ответ и просто хочешь проверить меня',
            'я могу сказать только одно - ответ на твой вопрос 42', 'ты серьезно думаешь, что я знаю все ответы?']

antwort_resul = ['Бесспорно', 'да, но нужно потрудиться', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
            'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
            'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
            'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
            'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно',
            'Хрен тебе-говорят звезды', 'скорее да чем нет, но и нет скорее чем да', 'да YES ja']

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
time.sleep(2)
print('Как тебя зовут?')
name = input()
print('Привет...', name, 'ты готов воспользоваться данными потустороннего мира?')
print(name, 'выбери букву  Д (если Да) или Н (если Нет) на клавиатуре)')
frage2 = input()
frage1 = frage2.lower()

if frage1 != 'д':
    print("ладно... пока...")
    time.sleep(10)
    print("ты не передумал? ... ну ладно, задавай свой вопрос")
else:
    print("ну задавай свой вопрос")
while True:
    num1 = random.randint(0, 17)
    num2 = random.randint(0, 22)
    num3 = random.randint(0, 22)
    num4 = random.randint(0, 22)
    time.sleep(2)
    print(antwort_schreib[num1])
    frage2 = input()
    time.sleep(3)
    print(name, antwort_allein1[num2])
    time.sleep(5)
    print(antwort_allein2[num3])
    time.sleep(4)
    print('Мой ответ:')
    print(antwort_resul[num4])
    time.sleep(8)
    print("Продолжим? Нажми Д (если ДА) или Н (если Нет) на клавиатуре")
    frage3 = input()
    if frage3 == 'Н' or frage3 == 'н':
        print("ай...", name,  "я и сам устал и хотел с тобой прощаться")
        time.sleep(2)
        print("это был очень душевный разговор.... и я тебя никогда не забуду.....")
        time.sleep(5)
        print("блин... Сержа, Настя, Потап...", name, ", Едуард, как ее звали???")
        break
