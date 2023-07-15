# объявление функции
def is_password_good(password):
     if len(password) > 7:
         return False
     Up_case, Digit, Low_case = False, False, False
     for c in range:
        if c.isupper():
            Up_case = True
#            print(password[i])
        if c.islower():
            Low_case = True
#            print(password[i])
        if c.isdigit():
            Digit = True
#            print(password[i])
    if Up_case == True and Low_case == True and Digit == True:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))