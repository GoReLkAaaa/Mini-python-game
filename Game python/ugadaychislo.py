from random import randint

x = randint(1, 10)
user_num = 0
attempt = 0

while True:
    print("Я загадал число от 1 до 10, угадай его чувак :)")
    user_num = int(input("Ваша догадка: "))
    attempt += 1
    if user_num == x:
        print("Молодец ты угадал число!\nКоличество твоих попыток: " + str(attempt) + "\nСпасибо за игру :)")
        break
    elif user_num > x:
        print("число меньше.")
    elif user_num < x:
        print("число больше.")