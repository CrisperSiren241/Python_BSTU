# Напишите программу, которая по номеру дня недели — целому числу от 1 до 7 — выдает в качестве результата количество занятий в вашей группе в соответствующий день.

operation = ""

while(operation != "0"):
    operation = input("Введите номер дня недели: ")
    match operation:
        case "1":
            print(f"У вас 1 лекция и 1 лабораторная по 1 неделе и 2 лекции и 1 лабораторная по 2 неделе")
        case "2":
            print(f"У вас 1 лекция и 2 лабораторные")
        case "3":
            print(f"У вас 3 лекции")
        case "4":
            print(f"У вас 1 лекция и 2 лабораторнын")
        case "5":
            print(f"У вас 1 лекция, 2 лабораторные и 1 занятие по физкультуре")
        case "6":
            print(f"У вас 1 практическое занятие и 1 лекция по 1 неделе и 1 лекция по 2 неделе")
        case "7":
            print(f"У вас нет занятий")