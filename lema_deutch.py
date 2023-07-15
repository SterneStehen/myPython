import spacy
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


def read_german_words_from_website(url):   # функция для скачивани текста с сайта
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        # Токенизация текста
        tokens = word_tokenize(text)

        # Фильтрация стоп-слов
        stop_words = set(stopwords.words('german'))
        filtered_tokens = [word for word in tokens if word.casefold() not in stop_words]

        # Стемминг слов
        stemmer = SnowballStemmer('german')
        stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

        # Отбор только немецких слов
        german_words = [word for word in stemmed_tokens if word.isalpha()]

        return ' '.join(german_words)
    else:
        print("Failed to retrieve text from the website.")
        return None
def lemmatize_german_text(text): # функция приводит слова к ифинитиву
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return " ".join(lemmas)
def remove_duplicates(words):  # функция убирает дубликаты слов
    return list(set(words))

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
#    print(words)
    return words


#s = 'Als Unterstützung für Geflüchtete, ehrenamtlich Lehrende und – natürlich DaZ-Kursleitende – stellen wir als weltweit führender Spezialist für Deutsch als Fremdsprache/Zweitsprache auf diesen Seiten Materialien und Tipps für einen schnellen, didaktisch-fundierten und praxiserprobten Deutsch-Unterricht für Sie zusammen.'
#s = "Eine Maus! Wir haben eine Maus! Eine Maus? Wie? Wo? In der Küche! Die Maus ist in der Küche! Wo ist sie? Hast du sie gesehen? Hast du die Maus gesehen - mit eigenen Augen? Nicht direkt gesehen. Aber ich weiß, da ist eine Maus. Ich bin sicher, da ist eine Maus! Wieso denn? Du hast sie doch gar nicht gesehen! Es ist wegen der Nutella. Das Nutellaglas war neulich noch ganz voll, jetzt ist es leer. Jemand hat die Nutella gegessen. Die ganze Nutella! Ich war’s nicht! Ich hab keine Nutella gegessen. Ich esse nie Nutella. Genau. Die Maus hat sie gegessen. Es ist eine Nutellamaus, die unsere ganze Nutella isst! Oh je.. wir haben eine Nutellamaus, das ist ja schrecklich...  Ja, das find ich auch schrecklich.  Genau, und es ist eine besonders schreckliche Maus.  Du meinst, die Maus ist besonders schrecklich?  Natürlich! Die Nutellamaus ist gigantisch, sie ist einen Meter achtzig groß und sie wiegt achtzig Kilo! Eine schreckliche, gigantische Riesenmaus! Du bist nämlich die Nutellamaus! Anna: Guten Morgen! Auch schon wach? Nicht wirklich... Es ist doch erst elf. Ich brauche jetzt erst mal nen Kaffee. Anna: Also ich verstehe nicht, wie man immer so lange schlafen kann. Wieso? Wann bist du denn aufgestanden?Anna: So gegen viertel vor sechs... Viertel vor - sechs? Wieso DAS denn? Anna: Ich liebe das! Raus aus den Federn und eine Runde joggen, danach eine kalte Dusche, ein kleines Frühstück... Um sieben sitze ich meist schon am Schreibtisch.  Um sieben? Am Schreibtisch? Ich finde es schon grausam, wenn ich um acht aufstehen muss! Anna: Der frühe Vogel fängt den Wurm. Bis du richtig wach bist, habe ich mein halbes Tagewerk erledigt. Unglaublich. Willst du denn nicht mal ausschlafen? Anna: Doch, klar. Sonntags schlafe ich manchmal bis halb acht!  Und das nennst du ausschlafen? Anna: Wir sind halt verschieden. Du bist eben eine Eule und ich - eine Lerche!  Hmm, soso… Übrigens: Dein Fahrrad ist wieder tipptopp. Ich habe es repariert, während du schon geschlafen hast. Bis halb drei morgens. Anna: Mein Fahrrad läuft wieder? Die alte Mühle? Das ist unglaublich. Danke! Ich liebe Eulen wie dich!"
#s1 = "1 Kaufen, kaufen, kaufen ... Was ist Ratenkauf? Lesen Sie den Text und kreuzen Sie an. © Man muss nicht sofort und auf einmal bezahlen, sondern man zahlt erst nach und nach. Die Ware kann man aber sofort mitnehmen. O Für Elektrogeräte wie Kühlschrank oder Spülmaschine gibt es ein spezielles Angebot: nehmen. Den Rest muss man bis zum 311. Man zahlt zuerst nur 50 € und kann das Gerät mit Ahle a . = -. Erfüll dir deine Wüns:..... on | gi \ merken \ een Unser Ratenkauf mach: - * k 5 — Endlich die neue Waschmaschine kaufen oder den Bu neuen Kühlschrank! Oder eine Spülmaschine? — Oder einfach das, was du dir schon so lange wünschst. Wie wäre es mit einem neuen schnelleren Computer ‘oder einem Riesen-Flachbildschirm, der dir deine Stars näher bringt? wi Heute schon mitnehmen und morgen erst bezahlen, e ) \ _ i ganz ohne Risiko: z.B. statt 1000 € auf einmal nur jeden Monat 50 € bezahlen. Nullprozentfinanzierung az noch bis zum 31.12. 2 Achmed hat bei Elektro-Mars eingekauft. 14)11 a Was hat Achmed gekauft? Hören Sie den Anfang eines Gesprächs und kreuzen Sie an. O Eine Waschmaschine. © Einen Kühlschrank. © Eine Spülmaschine. 14)12 _b Welche Argumente hören Sie? Hören Sie das Gespräch nun ganz und kreuzen Sie an. 1 Man muss nicht alles auf einmal bezahlen. 2 O Wenn man Zinsen zahlen muss, sollte man genau ausrechnen, wie viel mehr man am Ende bezahlt. 3 ODie kleine Summe, die man jeden Monat bezahlen muss, merkt man gar nicht. 4 O Die Verträge sind oft schwer zu verstehen. 5 O Man kauft schnell etwas und weiß am Ende nicht mehr, was man alles bezahlen muss. 6 O Man kauft vielleicht etwas, was man gar nicht braucht. 7 © Man kann mehr kaufen, weil man nur kleine Summen monatlich bezahlen muss. c Welche Argumente sprechen für den Ratenkauf, welche dagegen? Markieren Sie in b Argumente für den Ratenkauf und gegen den Ratenkauf. 3 Haben Sie schon einmal etwas auf Raten gekauft? Was? Warum (nicht)? Erzählen Sie."
# Пример использования функции
website_url = "https://www.thelanguageoffice.com/wp-content/uploads/2018/09/B1-Glossary.pdf"  # Замените на нужный URL
german_text_from_website = read_german_words_from_website(website_url)
if german_text_from_website:
    s1 = german_text_from_website
#    print(s1)

#s1 = "1 Kaufen, kaufen, kaufen ... Was ist Ratenkauf? Lesen Sie den Text und kreuzen Sie an. © Man muss nicht sofort und auf einmal bezahlen, sondern man zahlt erst nach und nach. Die Ware kann man aber sofort mitnehmen. O Für Elektrogeräte wie Kühlschrank oder Spülmaschine gibt es ein spezielles Angebot: nehmen. Den Rest muss man bis zum 311. Man zahlt zuerst nur 50 € und kann das Gerät mit Ahle a . = -. Erfüll dir deine Wüns:..... on | gi \ merken \ een Unser Ratenkauf mach: - * k 5 — Endlich die neue Waschmaschine kaufen oder den Bu neuen Kühlschrank! Oder eine Spülmaschine? — Oder einfach das, was du dir schon so lange wünschst. Wie wäre es mit einem neuen schnelleren Computer ‘oder einem Riesen-Flachbildschirm, der dir deine Stars näher bringt? wi Heute schon mitnehmen und morgen erst bezahlen, e ) \ _ i ganz ohne Risiko: z.B. statt 1000 € auf einmal nur jeden Monat 50 € bezahlen.   . Nullprozentfinanzierung az noch bis zum 31.12. 2 Achmed hat bei Elektro-Mars eingekauft. 14)11 a Was hat Achmed gekauft? Hören Sie den Anfang eines Gesprächs und kreuzen Sie an. O Eine Waschmaschine. © Einen Kühlschrank. © Eine Spülmaschine. 14)12 _b Welche Argumente hören Sie? Hören Sie das Gespräch nun ganz und kreuzen Sie an. 1 Man muss nicht alles auf einmal bezahlen. 2 O Wenn man Zinsen zahlen muss, sollte man genau ausrechnen, wie viel mehr man am Ende bezahlt. 3 ODie kleine Summe, die man jeden Monat bezahlen muss, merkt man gar nicht. 4 O Die Verträge sind oft schwer zu verstehen. 5 O Man kauft schnell etwas und weiß am Ende nicht mehr, was man alles bezahlen muss. 6 O Man kauft vielleicht etwas, was man gar nicht braucht. 7 © Man kann mehr kaufen, weil man nur kleine Summen monatlich bezahlen muss. c Welche Argumente sprechen für den Ratenkauf, welche dagegen? Markieren Sie in b Argumente für den Ratenkauf und gegen den Ratenkauf. 3 Haben Sie schon einmal etwas auf Raten gekauft? Was? Warum (nicht)? Erzählen Sie. Bevor die Gäste kommen, muss ich die Tische im Restaurant vorbereiten, das heißt, ich muss sie eindecken und dekorieren. Auch die Theke muss sauber und mit Getränken aufgefüllt sein. Was ich manchmal schwierig finde, ist, immer freundlich zu sein ‒ besonders wenn Gäste sich beschweren. Aber wahrscheinlich gibt es in jedem Beruf Dinge, die einem nicht so gut gefallen. Ich bin Andreas Aust. Ich mache hier im Restaurant „Biskus“ seit zwei Jahren meine Ausbildung zum Restaurantfachmann. In meinem Beruf bin ich vor allem für die Gäste da. Ich begrüße sie und bringe sie zu ihrem Tisch, nehme ihre Bestellungen auf und empfehle Gerichte von unserer Speisekarte. Verabschiedet Wortschatz etwas auf|nehmen hier: etwas notieren (z. B. eine Getränkebestellung) Ausbildung, -en (f.) Lehre; das Erlernen eines Berufs Auszubildende, -n/Auszubildende, jemand, der eine Ausbildung macht jemanden begrüßen zu jemandem „Hallo“ oder Ähnliches sagen; etwas, das man bei der Begrüßung zu jemandem sagt oder das man bei einer Begrüßung macht Beruf, -e (m.) Arbeit, Job, Tätigkeit sich beschweren sagen, dass man mit etwas nicht zufrieden ist Bestellung, -en (f.) hier: die höfliche Aufforderung an den Kellner, bestimmte Speisen oder Getränke zu bringen etwas dekorieren etwas schmücken einen Tisch ein|decken Besteck und Geschirr auf einen Tisch legen etwas empfehlen etwas loben; Werbung für etwas machen; sagen, dass man etwas sehr gut findet Gast, Gäste (m.) jemand, der zu Besuch ist (z. B in einem Restaurant) Gastraum, -räume (m.) hier: Raum oder Saal eines Restaurants, in dem die Gäste sitzen Gastronomie (f., nur Singular) der Bereich der Wirtschaft, zu dem Restaurants und Lokale gehören Gericht, -e (n.) Mahlzeit; verschiedene Lebensmittel, die z. B. gekocht und zusammen serviert werden Küchenchef, -s/Küchenchefin, -nen der Leiter/die Leiterin der Küche in einem Restaurant Küchenhilfe, -n (f.) jemand, der in einer Küche (z. B. in einem Restaurant) aushilft und arbeitet Lebensmittel, - (n.) die Nahrung; das Essen und die Getränke Restaurant, -s (n.) ein Ort, an dem man gegen Bezahlung an Tischen isst und trinkt und von einem Kellner bedient wird Restaurantfachmann, -männer/Restaurantfachfrau, -en jemand, der eine Ausbilung in der Gastronomie abgeschlossen hat Restaurantleiter, -/Restaurantleiterin, nen der Chef/die Chefin eines Restaurants etwas servieren hier: Gästen etwas bringen (z. B. Getränke) Speisekarte, -n (f.) eine Liste mit Gerichten und Getränken, die man z. B. in einem Restaurant bestellen kann (kurz: die Karte) Theke, -n (f.) hier: ein hoher Tisch in einem Restaurant, an dem z. B. Getränke zubereitet werden etwas vor|bereiten etwas soweit fertig machen, dass man es bald verwenden kann   etwas zapfen ein Getränk (meist Bier) aus einem Fass mit einem Zapfhahn in ein Glas füllen"
s = znack(s1) # убираем знаки


text = s.split(' ') # создаем массив
end = []


lemmatized_text = lemmatize_german_text(s)   # привеодим слова к инфинитиву
word_lem_s = lemmatized_text
word_lem_l = word_lem_s.split(' ')

for i in range(len(word_lem_l)): # убираем короткие слова
    if len(word_lem_l[i]) > 3:
        end.append(word_lem_l[i])


word_list = end                       # убираем дубликаты
result = remove_duplicates(word_list)



#print(lemmatized_text)
#print(word_lem_l)
#print(end)
print(result)