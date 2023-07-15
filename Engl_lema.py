import spacy
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def lemmatize_and_check(sentence):
    # Инициализация лемматизатора
    lemmatizer = nltk.WordNetLemmatizer()

    # Токенизация предложения на слова
    words = word_tokenize(sentence)

    # Массив для хранения верных лемматизированных слов
    valid_lemmas = []

    for word in words:
        # Лемматизация слова
        lemma = lemmatizer.lemmatize(word)

        # Проверка слова в словаре WordNet
        if wordnet.synsets(lemma):
            valid_lemmas.append(lemma)

    return valid_lemmas








def znack(words):  # убираем знаки
    words = words.replace(',', '')
    words = words.replace('.', '')
    words = words.replace(' – ', ' ')
    words = words.replace('!', '')
    words = words.replace('?', '')
    words = words.replace('–', '')
    words = words.replace('/', '')
    words = words.replace('-', ' ')
    words = words.replace('€', ' ')
    words = words.replace('©', ' ')
    words = words.replace('|', ' ')
    words = words.replace(':', ' ')
    words = words.replace('(', ' ')
    words = words.replace(')', ' ')
    return words


#s1 = "1 Kaufen, kaufen, kaufen ... Was ist Ratenkauf? Lesen Sie den Text und kreuzen Sie an. © Man muss nicht sofort und auf einmal bezahlen, sondern man zahlt erst nach und nach. Die Ware kann man aber sofort mitnehmen. O Für Elektrogeräte wie Kühlschrank oder Spülmaschine gibt es ein spezielles Angebot: nehmen. Den Rest muss man bis zum 311. Man zahlt zuerst nur 50 € und kann das Gerät mit Ahle a . = -. Erfüll dir deine Wüns:..... on | gi \ merken \ een Unser Ratenkauf mach: - * k 5 — Endlich die neue Waschmaschine kaufen oder den Bu neuen Kühlschrank! Oder eine Spülmaschine? — Oder einfach das, was du dir schon so lange wünschst. Wie wäre es mit einem neuen schnelleren Computer ‘oder einem Riesen-Flachbildschirm, der dir deine Stars näher bringt? wi Heute schon mitnehmen und morgen erst bezahlen, e ) \ _ i ganz ohne Risiko: z.B. statt 1000 € auf einmal nur jeden Monat 50 € bezahlen.   . Nullprozentfinanzierung az noch bis zum 31.12. 2 Achmed hat bei Elektro-Mars eingekauft. 14)11 a Was hat Achmed gekauft? Hören Sie den Anfang eines Gesprächs und kreuzen Sie an. O Eine Waschmaschine. © Einen Kühlschrank. © Eine Spülmaschine. 14)12 _b Welche Argumente hören Sie? Hören Sie das Gespräch nun ganz und kreuzen Sie an. 1 Man muss nicht alles auf einmal bezahlen. 2 O Wenn man Zinsen zahlen muss, sollte man genau ausrechnen, wie viel mehr man am Ende bezahlt. 3 ODie kleine Summe, die man jeden Monat bezahlen muss, merkt man gar nicht. 4 O Die Verträge sind oft schwer zu verstehen. 5 O Man kauft schnell etwas und weiß am Ende nicht mehr, was man alles bezahlen muss. 6 O Man kauft vielleicht etwas, was man gar nicht braucht. 7 © Man kann mehr kaufen, weil man nur kleine Summen monatlich bezahlen muss. c Welche Argumente sprechen für den Ratenkauf, welche dagegen? Markieren Sie in b Argumente für den Ratenkauf und gegen den Ratenkauf. 3 Haben Sie schon einmal etwas auf Raten gekauft? Was? Warum (nicht)? Erzählen Sie. Bevor die Gäste kommen, muss ich die Tische im Restaurant vorbereiten, das heißt, ich muss sie eindecken und dekorieren. Auch die Theke muss sauber und mit Getränken aufgefüllt sein. Was ich manchmal schwierig finde, ist, immer freundlich zu sein ‒ besonders wenn Gäste sich beschweren. Aber wahrscheinlich gibt es in jedem Beruf Dinge, die einem nicht so gut gefallen. Ich bin Andreas Aust. Ich mache hier im Restaurant „Biskus“ seit zwei Jahren meine Ausbildung zum Restaurantfachmann. In meinem Beruf bin ich vor allem für die Gäste da. Ich begrüße sie und bringe sie zu ihrem Tisch, nehme ihre Bestellungen auf und empfehle Gerichte von unserer Speisekarte. Verabschiedet Wortschatz etwas auf|nehmen hier: etwas notieren (z. B. eine Getränkebestellung) Ausbildung, -en (f.) Lehre; das Erlernen eines Berufs Auszubildende, -n/Auszubildende, jemand, der eine Ausbildung macht jemanden begrüßen zu jemandem „Hallo“ oder Ähnliches sagen; etwas, das man bei der Begrüßung zu jemandem sagt oder das man bei einer Begrüßung macht Beruf, -e (m.) Arbeit, Job, Tätigkeit sich beschweren sagen, dass man mit etwas nicht zufrieden ist Bestellung, -en (f.) hier: die höfliche Aufforderung an den Kellner, bestimmte Speisen oder Getränke zu bringen etwas dekorieren etwas schmücken einen Tisch ein|decken Besteck und Geschirr auf einen Tisch legen etwas empfehlen etwas loben; Werbung für etwas machen; sagen, dass man etwas sehr gut findet Gast, Gäste (m.) jemand, der zu Besuch ist (z. B in einem Restaurant) Gastraum, -räume (m.) hier: Raum oder Saal eines Restaurants, in dem die Gäste sitzen Gastronomie (f., nur Singular) der Bereich der Wirtschaft, zu dem Restaurants und Lokale gehören Gericht, -e (n.) Mahlzeit; verschiedene Lebensmittel, die z. B. gekocht und zusammen serviert werden Küchenchef, -s/Küchenchefin, -nen der Leiter/die Leiterin der Küche in einem Restaurant Küchenhilfe, -n (f.) jemand, der in einer Küche (z. B. in einem Restaurant) aushilft und arbeitet Lebensmittel, - (n.) die Nahrung; das Essen und die Getränke Restaurant, -s (n.) ein Ort, an dem man gegen Bezahlung an Tischen isst und trinkt und von einem Kellner bedient wird Restaurantfachmann, -männer/Restaurantfachfrau, -en jemand, der eine Ausbilung in der Gastronomie abgeschlossen hat Restaurantleiter, -/Restaurantleiterin, nen der Chef/die Chefin eines Restaurants etwas servieren hier: Gästen etwas bringen (z. B. Getränke) Speisekarte, -n (f.) eine Liste mit Gerichten und Getränken, die man z. B. in einem Restaurant bestellen kann (kurz: die Karte) Theke, -n (f.) hier: ein hoher Tisch in einem Restaurant, an dem z. B. Getränke zubereitet werden etwas vor|bereiten etwas soweit fertig machen, dass man es bald verwenden kann   etwas zapfen ein Getränk (meist Bier) aus einem Fass mit einem Zapfhahn in ein Glas füllen"
s1 = "June 12, 2023 at 8:00am CEST (Berlin Time).  Schedule for the first day 8:00am - 9:42am CEST: ID-Check, receive Campus Cards (Access Badges to the building) 9:42am CEST: Piscine Kickoff presentation, meet the team! 10:30am CEST: Access the Computers, and begin coding!  ID-Check The ID-Check is important, so we can verify your personal details, and hand out your access card to the 42 Heilbronn Campus building. Please arrive at the Campus between 8:00am and 9:00am.  CampusCard (building access card) The CampusCard is the access card you will receive on your first day. This card will allow you to enter the building 24/7 during your four-week Piscine, and can also be used to buy a subsidised lunch in the student lunchroom close to the Campus. You will be able to load money to your CampusCard balance, allowing you to pay for the lunches, and use vending machines on-site. To receive this CampusCard, you will have to register on the official BildungsCampus CampusCard platform. Please do so as soon as you receive this email! Otherwise, you might not be able to receive your access card on the first day of the Piscine.  Access Card Registration instructions To register your CampusCard, you will receive a separate email from the CampusCard platform. During this process, you will be prompted to do an online ID-Check. Please skip the ID-Check step, as this will be done on-site manually on your first day. There should be an option to do so. Also, make sure to upload a picture in the corresponding step! Without a picture, we can not print out your CampusCard. This picture will also be your profile picture for the duration of the Piscine, so don't forget to smile :). If you have any questions during this process, feel free to mail hello@42heilbronn.de, and we will happily assist you.  Please use the following information to fill out the registration form on the CampusCard Platform (see separate email): Your Function: Student Your Institution: 42 Heilbronn Your personnel/matriculation number: 387 Your family name (password): Moreronko  General Information What do you need to bring on the first day? The only thing you need to bring is an official ID-Card or Passport for verification. Other than that, everything else (Computers, mouse and keyboard, working environment) is provided by 42 Heilbronn. We would also recommend bringing a pair of Bluetooth headphones, as these are not provided by 42 Heilbronn, and can be a great thing to have in a busy working environment :).  Will there be a fixed schedule for the four-week Piscine? For most of the Piscine, you will be able to work on your projects independently, while managing your own time. The Campus is open 24/7, and you are allowed to study whenever you want. The only mandatory dates are the Kickoff day (ID-Check, presentation), exams on Friday (from 10:00am-18:00am), and Rush evaluations (will be scheduled individually each week starting week 2, so staying flexible during the day is important). While you do have a lot of flexibility during the Piscine, we do recommend setting up a personal schedule, and working with it. Organization is key during this time. Since this is a full-time program, it is still highly recommended to cancel all other obligations during these four weeks.  How should you prepare for these four weeks? Clear your schedule! Make sure you have no other distractions for these four weeks, as it is a full-time, 7-day per week program. Make sure you have your personal life organised beforehand. This means ensuring you have enough budget for cost of living (meals, etc.), a place to stay (or to commute), and, if you are moving to Heilbronn for these four weeks, have everything else you need (clothes, sanitary items, etc.). You do not need to practice coding before the Piscine! The Piscine starts off with beginner-level projects, so you do not need to worry if you have never had anything to do with IT before. There will be enough other peers that can help you out if you are stuck :)  The entire team is already excited to meet you! You can already get excited about an intense, but extremely educational and fun four-weeks at the 42 Heilbronn Campus. As always, never hesitate to reach out to hello@42heilbronn.de if you have any questions, or need any assistance at all. See you in next week!  Best Regards Andreas from 42 Heilbronn"



s = znack(s1) # убираем знаки
# Пример использования функции
input_sentence = s
end = []
word_lem_l = lemmatize_and_check(input_sentence)
for i in range(len(word_lem_l)): # убираем короткие слова
    if len(word_lem_l[i]) > 3:
        end.append(word_lem_l[i])

print(end)