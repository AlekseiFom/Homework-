def square(s):
        return s * s
side = float(input("Введите длину стороны: ").replace(',', '.'))
result = round(square(side))

print(f"Площадь: {result}")

