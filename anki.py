
"""
from german_lemmatizer import lemmatize
german_lemmatizer.lemmatize
def lemmatize(texts: {__len__},
              chunk_size: int = 10000,
              working_dir: str = ".",
              escape: bool = False,
              n_jobs: int = 1,
              remove_stop: bool = False) -> Generator[str, Any, None]

"""
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):
    if treebank_tag=='VBN':
        return 'v'
    elif treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''
import nltk
from nltk.stem import WordNetLemmatizer
s = "Once you’ve created your data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. This document explains how to use this API. Refer to the data model reference for full details of all the various model lookup options."
#s = s.replace(',', '')
#s = s.replace('.', '')
#s = s.replace('-', '')
#s = s.replace('!', '')
#s = s.replace('?', '')
#s = s.lower()
#symbol = [',', ' ', '!', '?', '-', '.', ':']
#    for c in symbol:
#        s = s.replace(c, '')
s1 = ''
for i in range(len(s)):
    if s[i]=='.' or s[i]==':' or s[i]==',' or s[i]=='!' or s[i]=='?':
        continue
    s1 = s1 + s[i]
lis = s1.split(' ')
lematieser = WordNetLemmatizer()
#print(lematieser.lemmatize('created', 'v'))

wnl = WordNetLemmatizer()
from nltk import word_tokenize, pos_tag
word_tokenize(s1)
tagget_words = pos_tag(lis)
#word, pos = lis2[2]
word = 'created'
pos = 'VBN'
#print(get_wordnet_pos(pos))
print(lematieser.lemmatize(word, get_wordnet_pos(pos)))
#lis2 = lis2.replace('NNP', 'N')
#print(pos)
print(tagget_words)
print(s1)
print(lis)
from nltk import sent_tokenize
sentences = sent_tokenize(s)
