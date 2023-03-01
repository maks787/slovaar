countries_dict = {
    "Австрия": "Вена",
    "Бельгия": "Брюссель",
    "Великобритания": "Лондон",
    "Германия": "Берлин",
    "Ирландия": "Дублин",
    "Лихтенштейн": "Вадуц",
    "Нидерладны": "Амстердам",
    "Франция": "Париж",
    "Белоруссия": "Минск",
    "Болгария": "София",
    "Польша": "Варшава",
    "Чехия": "Прага",
    "Албания": "Тирана",
    "Босния и Герцеговина": "Сараево",
    "Северная Македония": "Скопье",
    "Сербия": "Белград"
}
import random
def countries(dictionary, v):
    if v == "1":
        capital = input("Введите название столицы: ")
        for key, value in dictionary.items():
            if value == capital:
                print("Страна: ", key)
                return
        print("Такой столицы нет в списке.")
    elif v == "2":
        country = input("Введите название страны: ")
        if country in dictionary:
            print("Столица: ", dictionary[country])
        else:
            print("Такой страны нет в списке.")
    else:
        print("Некорректный ввод.")

def new_key_value(dictionary):
    key = input("Введите название страны: ")
    value = input("Введите название столицы: ")
    dictionary[key] = value
    print("Запись добавлена в словарь.")

def correct_errors(dictionary):
    key = input("Введите название страны или столицы, которую нужно исправить: ")
    if key in dictionary:
        new_value = input("Введите новое значение: ")
        dictionary[key] = new_value
        print("Значение изменено.")
    else:
        print("Такой записи нет в словаре.")
def test_knowledge(countries_dict):
    correct_answers=0
    total_questions=0
    while True:
        question_type=input("1 - Столица или 2 - Страна? ")
        if question_type=="1":
            question=random.choice(list(countries_dict.values()))
            answer=input(f"Назовите страну, столицей которой является {question}: ")
            for key,value in countries_dict.items():
                if value==question:
                    if answer==key:
                        print("Правильно!")
                        correct_answers+=1
                    else:
                        print(f"Неправильно. Правильный ответ: {key}")
                    total_questions+=1
                    break
            else:
                print("Произошла ошибка. Попробуйте еще раз.")
        elif question_type=="2":
            question=random.choice(list(countries_dict.keys()))
            answer=input(f"Назовите столицу страны {question}: ")
            if answer==countries_dict[question]:
                print("Правильно!")
                correct_answers+=1
            else:
                print(f"Неправильно. Правильный ответ: {countries_dict:[answer]}")