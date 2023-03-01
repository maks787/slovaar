from module1 import *
while True:
    print("Привет! Пройдёмся по странам и их столицам!")
    print("1 - Узнать столицу страны или наоборот,\n2 - Добавить новую страну и столицу,\n3 - Исправить ошибку,\n4 - Проверь свои знания")
    menu = input()
    if menu == "1":
        v = input("Будем искать страну по стoлице(1) или стoлицу по стране(2)? ")
        countries(countries_dict, v)
    elif menu == "2":
        new_key_value (countries_dict)
    elif menu == "3":
        correct_errors(countries_dict)
    elif menu == "4":
        test_knowledge(countries_dict)
        # code for the knowledge test
        pass
    else:
        print("Некорректный ввод.")
