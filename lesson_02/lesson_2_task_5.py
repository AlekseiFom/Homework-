while True:
    try:
        nl = int(input("Введите номер месяца (1-12): "))
        if 1 <= nl <= 12:
            break
        else:
            print("Ошибка! Введите число от 1 до 12.")
    except ValueError:
        print("Это не число!")

def month_to_season(n):
    if n in [1, 2, 12]:
        print("Зима")
    elif n in [3,4,5]:
        print("Весна")
    elif n in [6, 7, 8]:
        print("Лето")
    else:
        print("Осень")

month_to_season(nl)