import random

words = [
    {'german': 'Buchung', 'russian': 'бронирование', 'example': 'Die Buchung wurde bestätigt.', 'part_of_speech': 'Substantiv'},
    {'german': 'begrüßen', 'russian': 'приветствовать', 'example': 'Ich möchte Sie herzlich begrüßen.', 'part_of_speech': 'Verb'},
    'Buchung', 'begruss', 'Reservierenetwa', 'Wunsch', 'Gast', 'Seinetwas', 'Saal', 'Telefonanschluss', 'deutsch', 'reservieren', 'Sagenub', 'lernenub', 'dabei', 'alternativ', 'lern', 'noti', 'Vorzuschlag', 'freundlich', 'Lektion', 'Zurucksetzenkursubersicht', 'Aufzuford', 'frei', 'Absag', 'Copycreated', 'Vorhand', 'Gesellschaft', 'annehm', 'Reservier', 'Mantel', 'Ander', 'Tischnumm', 'verwenden', 'Bitt', 'informi', 'Zahl', 'Grupp', 'Prozess', 'extern', 'Buch', 'with', 'Wann', 'zugeordnen', 'Okay', 'Einverstand', 'Lektionnavigation', 'Unspartnerservicenewsletterpodcastskontaktfind', 'Folgenjemand', 'Treff', 'geben', 'erwaren', 'Komm', 'herzlich', 'Telefon', 'Handy', 'Geschloss', 'Angegeb', 'Hinterhergeh', 'This', 'mehr', 'zeitpunkt', 'leid', 'shap', 'jemand', 'Jack', 'lernendeutsch', 'Platz', 'barrierefrei', 'storni', 'Telefonierenmit', 'Mitzukomm', 'Folg', 'zuordnen', 'Wortschatz', 'Frag', 'Verabschied', 'enabl', 'vorbestellen', 'need', 'Ausgebuchtso', 'konnen', 'akzepti', 'vorbestell', 'Modifikation', 'Person', 'Vorschlag', 'Navigationreservierungin', 'restaurant', 'Welledatenschutzimpressumerklar', 'Sprech', 'Bescheid', 'aufbewahren', 'abschliessenshap', 'Wurd', 'auss', 'Tisch', 'Mocht', 'Rechn', 'Garderob', 'Telefonnumm', 'zahlenfolg', 'Javascript', 'mieten', 'Willkomm', 'Find', 'lernentoggl']

def add_article(word):
    if word['part_of_speech'] == 'Substantiv':
        article = 'der' if word['german'][0].isupper() else 'die'
        word['german'] = article + ' ' + word['german']

# Исключение слов уровня А1 (пример)
def exclude_a1_words(words):
    excluded_words = ['das', 'ist', 'ein', 'eine']  # Пример исключенных слов уровня А1
    return [word for word in words if word['german'] not in excluded_words]

def create_table(words):
    table = []
    for word in words:
        add_article(word)
        table.append([word['german'], word['russian'], word['example'], word['part_of_speech']])
    return table

# Исключение слов уровня А1
words = exclude_a1_words(words)

# Перемешивание слов
random.shuffle(words)

# Создание таблицы
table = create_table(words)

# Вывод таблицы
for row in table:
    print(row)