# put your python code here
# put your python code here
import random
def is_valid(num1):
    return (0<num1<101)


def play1(count):

    x = random.randint(1, 100)
#    count = 0
    while True:
        n = int(input())
        if is_valid(n) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
        elif n < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif n > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        elif x == n:
            print('Вы угадали, поздравляем!')
            break
    print('Спасибо, что играли в числовую угадайку. Для отгадывания вам понадобилось', count, 'попыток.')
    print('Вы выграли Суперприз! возможность сделать Сереже Миньет!!!')
    return('если вы хотите повторить, введите Д, если нет, введите Н')

print('Добро пожаловать в числовую угадайку')
print("Hübschen Frau:)")
print('У вас есть возможность выграть суреприз!..... готовы?')
print("Тогда вам необходимо угать число от 1 до 100... введите число и нажмите ENTER)")
print(play1(0))


antwort = int(input())
x = 1
if antwort == x:
    print('попробуем угадать. как вы думаете, какое у нас чило?')

    play1(0)
else:
    print('С тобой весело, спасибо, что поиграл')


#else:
#65
# print('До свидания')
