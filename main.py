import os

banner = """

╔═╗░╔╗░░░  ╔═══╗░░░░░░░░░░
║║╚╗║║░░░  ║╔══╝░░░░░░░░░░
║╔╗╚╝╠══╗  ║╚══╦═╦══╦╦═══╗
║║╚╗║║╔╗║  ║╔══╣╔╣║═╬╬══║║
║║░║║║╚╝║  ║║░░║║║║═╣║║══╣
╚╝░╚═╩══╝  ╚╝░░╚╝╚══╩╩═══╝

┌───────────────────────┐
│Разработчик: @Fr31zep  │
└───────────────────────┘
┌───────────────────────┐
│[1] Поиск по номеру    │
│[2] Поиск по IP        │
│[3] Генерация личности │
│[4] Генерация карты    │
│[5] Информация         │
│[99] Выйти             │
└───────────────────────┘

"""

print(banner)

choice = input("[?] Введите номер желаемой функции -> ")

if choice == "1":
    os.system("clear")
    os.system("python number.py ")
if choice == "2":
    os.system("clear")
    os.system("python ip.py")
if choice == "3":
    os.system("clear")
    os.system("python generate.py")
if choice == "4":
    os.system("clear")
    os.system("python card.py")
if choice == "5":
    os.system("clear")
    os.system("python info.py")
if choice == "99":
    os.system("clear")
    os.system("python quit.py")
    
    
