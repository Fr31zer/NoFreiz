import os
import random
import time

yesorno = input("Вы желаете установить необходимые библиотеки? Yes/No: ")

if yesorno == "Yes":
    os.system("pip install colorama")
    os.system("pip install faker")
    os.system("pip install colored")
    os.system("pip install pystyle")
    os.system("pip install random")
    os.system("pip install time")
    os.system("pip install urllib")
    os.system("pip install json")
    os.system("pip install urllib.requrest")
    os.system("pip install requrest")
    os.system("clear")
    os.system("python main.py")

if yesorno == "No":
    print("Вам необходимо обновить или установить необходимые библиотеки")
    time.sleep(7)
    os.system("clear")
    os.system("python nofreiz.py")
    
