a = input("Введите число: ")

if a.isdigit():
    if int(a) % 2 == 0:
        print(f"Число {a} является четным")
    else:
        print(f"Число {a} не является четным")
else:
    print("Ошибка: введено не число")