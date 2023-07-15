from gettext import install

import pip
import setuptools
import spacy as spacy
from pip._internal.cli.cmdoptions import python

nlp = spacy.load('de_core_news_md')

mails=['Hallo. Ich spielte am frühen Morgen und ging dann zu einem Freund. Auf Wiedersehen', 'Guten Tag Ich mochte Bälle und will etwas kaufen. Tschüss']

mails_lemma = []

for mail in mails:
     doc = nlp(mail)
     result = ' '.join([x.lemma_ for x in doc])
     mails_lemma.append(result)
print(mails, mails_lemma)