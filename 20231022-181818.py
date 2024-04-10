import random
import time

def ruletka():
    global bank_d
    global bank_p
    def rulet(bet, collor):
        time.sleep(0.5)
        z = random.randint(0, 36)
        global bank_d
        global bank_p
        if z == 0:
            print(f'Выпало число: {z} green')
            if collor == 'g':
                bank_p += bet * 14
                bank_d -= bet * 14
                print(f'Вы выйграли: {bet * 14}$')
            else:
                bank_d += bet
                print(f'Вы проиграли: {bet}$')
        elif z % 2 == 0:
            print(f'Выпало число: {z} black')
            if collor == 'b':
                bank_p += bet * 2
                bank_d -= bet * 2
                print(f'Вы выйграли: {bet * 2}$')
            else:
                bank_d += bet
                print(f'Вы проиграли: {bet}$')
        elif z % 2 != 0:
            print(f'Выпало число: {z} red')
            if collor == 'r':
                bank_p += bet * 2
                bank_d -= bet * 2
                print(f'Вы выйграли: {bet * 2}$')
            else:
                bank_d += bet
                print(f'Вы проиграли: {bet}$')
    print('Это упрощённая версия рулетки, для выбора цвета пишите "r"-red, "g"-green, "b"-black')
    print('Ваша цель обанкротить казино)')
    c = 'rgb'
    while True:
        print('__________________________')
        if bank_p > bank_all:
            print(f'Ваш счёт равен: {bank_all}$')
        if bank_p <= bank_all:
            print(f'Ваш счёт равен: {bank_p}$')
        print(f'Счёт казино: {bank_d}$')
        if bank_p == 0:
            print('Увы вы стали бомжом. Прочь из казика!')
            break
        if bank_d <= 0:
            print('Вы обанкротили казино!')
            break
        while True:
            bet = float(input('Введите вашу ставку:'))
            collor = input('Введите ваш цвет:')
            if collor not in c or float(bet) > bank_p or float(bet) > bank_d:
                print('Ошибка! респин')
            else:
                bank_p -= bet
                rulet(bet, collor)
                break

def miner():
    global bank_d
    global bank_p
    kef = {25: 1, 24: 1.01, 23: 1.02, 22: 1.04, 21: 1.08, 20: 1.16,
        19: 1.32, 18: 1.64, 17: 1.86, 16: 2, 15: 2.16, 14: 2.32,
        13: 2.64, 12: 3, 11: 3.32, 10: 3.86, 9: 4, 8: 4.64,
        7: 5, 6: 5.64, 5: 6, 4: 6.86, 3: 8, 2: 10, 1: 30
        }
    min_pole = [[[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []]]
    min_pole1 = [[['⬛'], ['⬛'], ['⬛'], ['⬛'], ['⬛']],
                [['⬛'], ['⬛'], ['⬛'], ['⬛'], ['⬛']],
                [['⬛'], ['⬛'], ['⬛'], ['⬛'], ['⬛']],
                [['⬛'], ['⬛'], ['⬛'], ['⬛'], ['⬛']],
                [['⬛'], ['⬛'], ['⬛'], ['⬛'], ['⬛']]]
    while True:
        bomb = int(input('Введите кол-во бомб:'))
        if 0 < bomb < 25:
            break
        else:
            print('Ошибка! бомб может быть от 1 до 24')
    b = bomb
    while True:
        bet = float(input('Введите вашу ставку:'))
        if bet > bank_p:
            print('У вас нет столько денег')
        else:
            break
    while True:
        if bomb == 0:
            break
        c = random.randint(0, 4)
        v = random.randint(0, 4)
        if len(min_pole[c][v]) == 0:
            min_pole[c][v] += '💣'
            bomb -= 1
    for z in range(len(min_pole)):
        for x in range(len(min_pole[z])):
            if len(min_pole[z][x]) == 0:
                min_pole[z][x] += '💎'
    cristal = 0
    fl = 0
    while True:
        if fl == 1:
            break
        for z in range(len(min_pole)):
            for x in range(len(min_pole[z])):
                if '💎' in min_pole[z][x]:
                    cristal += 1
        fl = 1
    c = 0
    while True:
        for z in range(len(min_pole1)):
            for x in range(len(min_pole1[z])):
                print(*min_pole1[z][x], end='')
            print()
        for z in range(len(min_pole1)):
            if c == 1:
                break
            for x in range(len(min_pole1[z])):
                if '💣' in min_pole1[z][x]:
                    print(f'Вы проиграли: {bet}')
                    bank_d += bet
                    min_pole[z][x] = '💥' # type: ignore
                    c = 1
                if c == 1:
                    break
        if c == 1:
            break
        brt = 0
        while True:
            print(f'Желаете забрать: {bet * kef[cristal]}')
            gr = input('Y или N:')
            if gr.lower() == 'y':
                bank_p += bet * kef[cristal]
                print(f'Вы вйграли: {bet * kef[cristal]}')
                brt = 1
                break
            elif gr.lower() == 'n':
                break
        if brt == 1:
            break
        if cristal == 0:
            print('Вы разминировали всё поле!')
            bank_p += bet * kef[cristal]
            print(f'Вы вйграли: {bet * kef[cristal]}')
        print(f'Коэф равен: {kef[cristal]}x')
        while True:
            y = int(input('Введите координату "y":'))
            x = int(input('Введите координату "x":'))
            if '⬛' in min_pole1[y - 1][x - 1]:
                min_pole1[y - 1][x - 1] = min_pole[y - 1][x - 1]
                if '💎' in min_pole[y - 1][x - 1]:
                    cristal -= 1
                break
            elif '⬛' not in min_pole1[y - 1][x - 1]:
                print('Данная клетка уже открыта!')
    for z in range(len(min_pole)):
            for x in range(len(min_pole[z])):
                print(*min_pole[z][x], end='')
            print()
bank_p = float(input('Выберете сумму денег игрока:'))
bank_d = float(input('Выберете сумму денег диллера:'))
bank_all = bank_p + bank_d
game = input()
if game.lower() == 'рулетка':
    ruletka()
elif game.lower() == 'минёр':
    miner()
print(bank_p)