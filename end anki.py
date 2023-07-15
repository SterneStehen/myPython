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

#text = "Once you’ve created your data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. This document explains how to use this API. Refer to the data model reference for full details of all the various model lookup options."
#text = "In a midLS file, place the command line that will list all files and directories in your current directory (except for hidden files or any file that starts by a dot - yes, that includes double-dots), separated by a comma and a space, by order of modification date. Make sure the directory’s names are followed by a slash character. What has not been asked for should not be done "
#text = "Milestone Achieved, Keep Going! You have reached the end of the mandatory exercises to validate this project. It’s up to you to decide if you want to continue with the following optional exercises or switch to your next project. Both paths will make you see useful elements one day or another. To make your choice please consider the following elements: • The very first exam is about C programming. So you may have already experienced the very first C project before. Same for the rush at the end of the week (you’ll learn soon about the rush). • Your excellence in this Piscine will be evaluated on multiple factors. The completion of each project is one of them, but the overall progress through the entire list of projects of the Piscine is another. Choose wisely to optimize your results. • It will always be possible to try the same project again in a couple of days/weeks, until the end of the Piscine. • Keeping synchronised with your peers ensure a better collaboration."
text = "Chapter II  Foreword  Cod liver oil is a nutritional supplement derived from liver of cod  fish (Gadidae). " \
       " As with most fish oils, it has high levels of the omega-3 fatty acids,  eicosapentaenoic acid (EPA) and docosahexaenoic acid (DHA).  Cod liver oil also contains vitamin A and vitamin D.  " \
       "It has historically been taken because of its vitamin A and vitamin D content.  It was once commonly given to children, because vitamin D has been shown to  prevent rickets and other symptoms of vitamin D deficiency.  Contrary to Cod liver oil, C is good, eat some!  4  Chapter III  Exercice 00: ft_putchar  Exercise 00  ft_putchar  Turn-in directory : ex00/  Files to turn in : ft_putchar.c  Allowed functions : write  • Write a function that displays the character passed as a parameter.  • It will be prototyped as follows :  void ft_putchar(char c);  To display the character, you must use the write function as follows.  write(1, &c, 1);  The first retry delay is short, do not hesitate to " \
       "trigger an  intermediate evaluation to measure your progress.  5  Chapter IV  Exercise 01: ft_print_alphabet  Exercise 01  ft_print_alphabet  Turn-in directory : ex01/  Files to turn in : ft_print_alphabet.c  Allowed functions : write  • Create a function that displays the alphabet in lowercase, on a single line, by  ascending order, starting from the letter ’a’.  • Here’s how it should be prototyped :  void ft_print_alphabet(void);  Do not hesitate to pickup randomly someone in your cluster to ask a  question.  6  Chapter V  Exercise 02:  ft_print_reverse_alphabet  Exercise 02  ft_print_reverse_alphabet  Turn-in directory : ex02/  Files to turn in : ft_print_reverse_alphabet.c  Allowed functions : write  • Create a function that displays the alphabet in lowercase, on a single line, by  descending order, starting from the letter ’z’.  • Here’s how it should be prototyped :  void ft_print_reverse_alphabet(void);  Git push regularly.  7  Chapter VI  Exercise 03: ft_print_numbers  Exercise 03  ft_print_numbers  Turn-in directory : ex03/  Files to turn in : ft_print_numbers.c  Allowed functions : write  • Create a function that displays all digits, on a single line, by ascending order.  • Here’s how it should be prototyped :  void ft_print_numbers(void);  Collaboration is a key to success.  8  Chapter VII  Exercise 04: ft_is_negative  Exercise 04  ft_is_negative  Turn-in directory : ex04/  Files to turn in : ft_is_negative.c  Allowed functions : write  • Create a function that displays ’N’ or ’P’ depending on the integer’s sign entered  as a parameter. If n is negative, display ’N’. If n is positive or null, display ’P’.  • Here’s how it should be prototyped :  void ft_is_negative(int n);  Failure is part of your learning journey.  9  C Piscine C 00  Milestone Achieved, Keep Going!  You have reached the end of the mandatory exercises to validate this project.  It’s up to you to decide if you want to continue with the following optional " \
       "exercises  or switch to your next project. Both paths will make you see useful elements one day or  another.  To make your choice please consider the following elements:  • The very first exam is about C programming. So you may have already experienced  the very first C project before. Same for the rush at the end of the week (you’ll  learn soon about the rush).  • Your excellence in this Piscine will be evaluated on multiple factors. The completion  of each project is one of them, but the overall progress through the entire list of  projects of the Piscine is another. Choose wisely to optimize your results.  • It will always be possible to try the same project again in a couple of days/weeks,  until the end of the Piscine.  • Keeping synchronised with your peers ensure a better collaboration.  10  Chapter VIII  Exercise 05: ft_print_comb  Exercise 05  ft_print_comb  Turn-in directory : ex05/  Files to turn in : ft_print_comb.c  Allowed functions : write  • Create a function that displays all different combinations of three different digits in  ascending order, listed by ascending order - yes, repetition is voluntary.  • Here’s the intended output :  $>./a.out | cat -e  012, 013, 014, 015, 016, 017, 018, 019, 023, ..., 789$>  • 987 isn’t there because 789 already is.  • 999 isn’t there because the digit 9 is present more than once.  • Here’s how it should be prototyped :  void ft_print_comb(void);  Did you check with your right neighbor ?  11  Chapter IX  Exercise 06: ft_print_comb2  Exercise 06  ft_print_comb2  Turn-in directory : ex06/  Files to turn in : ft_print_comb2.c  Allowed functions " \
       " write  • Create a function that displays all different combination of two two digits numbers  (XX XX) between 00 and 99, listed by ascending order.  • Here’s the expected output :  $>./a.out | cat -e  00 01, 00 02, 00 03, 00 04, 00 05, ..., 00 99, 01 02, ..., 97 99, 98 99$>  • Here’s how it should be prototyped :  void ft_print_comb2(void);  Get inspired by others, do not let them do your job.  12  Chapter X  Exercise 07: ft_putnbr  Exercise 07  ft_putnbr  Turn-in directory : ex07/  Files to turn in : ft_putnbr.c  Allowed functions : write  " \
       " Create a function that displays the number entered as a parameter. The function  has to be able to display all possible values within an int type variable.  • Here’s how it should be prototyped :    Do not believe any source of information: always make your own  tests, controls and verifications.  13  Chapter XI  Exercise 08: ft_print_combn  Exercise 08  ft_print_combn  Turn-in directory : ex08/  Files to turn in : ft_print_combn.c  Allowed functions : write  • Create a function that displays all different combinations of n numbers by ascending  order.  • n will be so that : 0 < n < 10.  • If n = 2, here’s the expected output :  $>./a.out | cat -e  01, 02, 03, ..., 09, 12, ..., 79, 89$>  • Here’s how it should be prototyped :  void ft_print_combn(int n);  Did you check with your left neighbor ?  14  Chapter XII  Submission and peer-evaluation  " \
                                                                                                                                                                                                                                                                                   "Turn in your assignment in your Git repository as usual. Only the work inside your repository will be evaluated during the defense. Don’t hesitate to double check the names of  your files to ensure they are correct.  You need to return only the files"
from nltk import sent_tokenize #разбивка текста на предложения, перевод в масив
sentences = sent_tokenize(text)
#print(sentences)

from nltk import word_tokenize, pos_tag #разбивка 1-го предложения на слова

tagget_sentence = pos_tag([w.lower() for w in word_tokenize(sentences[0]) if len(w) >1]) #определяем часть речи
#tagget_words = pos_tag(tagget_sentence)
#print(tagget_sentence)

import nltk
from nltk.stem import WordNetLemmatizer #приводим слова к инфинитиву
lemmatiezer = WordNetLemmatizer()
word, pos = tagget_sentence[-1]
words = [lemmatiezer.lemmatize(word, get_wordnet_pos(pos)) for (word, pos) in tagget_sentence if get_wordnet_pos(pos)]
all_words = []
for sentence in sentences:
    tagget_sentence = pos_tag([w.lower() for w in word_tokenize(sentence) if len(w) > 1])
    sentence_words = [lemmatiezer.lemmatize(word, get_wordnet_pos(pos)) for (word, pos) in tagget_sentence if get_wordnet_pos(pos)]
    all_words = all_words + sentence_words

from nltk.corpus import brown # проверяем слова по словарю брауна и удаляет сленг
brown.words()
brown_words = set(brown.words())
base_words = [w for w in all_words if w in brown_words]
print(base_words, all_words, len(all_words), sep ='\n')

