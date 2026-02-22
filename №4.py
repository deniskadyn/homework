while 1:
    a = input("Введите число: → ")
    if a == "exit":
        print("Выход из программы...")
        break
    if a.lstrip('-').isdigit():
        print("В этом числе", len(a) - (a[0] == "-"), "цифры.")
    else:
        print("Ошибка: данные не являются числом.")