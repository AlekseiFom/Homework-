def is_year_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
year = int(input("Введите год:"))

result = is_year_leap(year)

print("Год:", year, result )
