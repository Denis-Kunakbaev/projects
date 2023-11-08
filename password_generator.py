import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

answer = 'д'
password_amount = int(input('Сколько паролей будем генерировать?'))
lenght_password = int(input('Какая должна быть длина пароля?'))
digits_in_password = input('Цифры в пароле будут?')
upper_in_password = input('Как на счет заглавных букв?')
lower_in_password = input('Строчные добавляем?')
punct_in_password = input('А символы?')
similar_in_password = input('Неоднозначные символы будут?')

if digits_in_password == answer:
    chars += digits
if upper_in_password == answer:
    chars += uppercase_letters
if lower_in_password == answer:
    chars += lowercase_letters
if punct_in_password == answer:
    chars += punctuation
if similar_in_password == answer:
    for s in 'il1Lo0O':
        chars.replace(s,'')

def generate_password():
    password = ''
    for i in range(1,lenght_password+1):
        c = random.choice(chars)
        password += c
    return password
for i in range(password_amount ):
    print(generate_password())
