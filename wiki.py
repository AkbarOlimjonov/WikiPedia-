
from termcolor import cprint,colored
import pyfiglet 
import wikipedia
import os,sys

wikipedia.set_lang('uz')
menu_one = "[1] Qidirish"
menu_two = "[2] Telegram"

menu = f"{menu_one} \n{menu_two}"

result = pyfiglet.figlet_format("WikiPedia") 

cprint(result,'green')

cprint(menu,'red')

def systemcommand():
    if sys.platform=="win32":
        os.system('cls')
    else:
        os.system('clear')
    

def search():
    while True:
        text = colored('[?] Ozingizni qiziqtirgan maqolani izlang: ', 'green')
        select = input(text)
        if select == "":
            cprint("[Error] Hech narsa kiritilmadi!",'red')
            systemcommand()
            cprint(result,'green')
            cprint(menu,'red')
            return 
            
            
        os.system('clear')
        cprint(result,'green')
        print(wikipedia.summary(select))
def main():
    while True:
        text = colored('[$] Menularni birini tanlang: ', 'yellow')
        select = input(text)
        if select == "1":
            os.system('clear')
            cprint(result,'red')
            search()
        elif select == "2":
            print("https://t.me/Admn_Mars")
        

main()