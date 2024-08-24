 # выбираем слово
import random

word = random.choice(['колобок', 'пирожок', 'огурец','игрушка'])

# генерируем список с заглушками
word_list = ['_' for i in word] #это тот же цикл for, который ниже
# for i in word:
#     word_list.append('_')
print(word_list)

# предлагаем угадать букву
lifes = 3
while lifes > 0:
    user_letter = input('введите букву: ')
    find_letter = False
    for index, letter in enumerate(word):
        if user_letter == letter:
            find_letter = True
            word_list[index] = letter

    if not find_letter:
        lifes -= 1
        print('не угадал')
    print(f'осталось {lifes} попыток')

    user_word = ''.join(word_list)
    print(user_word)

    if user_word == word:
        print('отгадал')
        break
else:
    print('ты проиграл')


