import random
def guess_game():
    random_number = random.randint(1,100)
    a = int(input("введите число:"))
    while True :
        if (a == random_number):
            print("Вы угадали!")
            break
        elif (a < random_number):
            a = int(input("введите число побольше:"))
        else:
            a=int(input("введите число поменьше:"))

guess_game()