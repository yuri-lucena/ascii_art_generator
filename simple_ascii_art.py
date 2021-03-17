"""
################################################################
#####################  CREATED BY BEARLIM  #####################
################################################################
"""
import os 
import sys
import platform
import time
try:
    import art
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
except ModuleNotFoundError:
    # Checking the python version
    v = sys.version_info
    if platform.system() == "Windows":
        os.system("py.exe -m pip install art")
        os.system("py.exe -m pip install --upgrade art")
        os.system("py.exe -m pip install colorama")
        os.system("py.exe -m pip install --upgrade colorama")
    elif platform.system() == "Linux":
        os.system(f"python{v[0]}.{v[1]} -m pip install art")
        os.system(f"python{v[0]}.{v[1]} -m pip install --upgrade art")
        os.system(f"python{v[0]}.{v[1]} -m pip install colorama")
        os.system(f"python{v[0]}.{v[1]} -m pip install --upgrade colorama")
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
    

def start():
    try:
        banner =             f'''
             {Fore.RED}@@@@@@    @@@@@@    @@@@@@@  @@@  @@@  
            @@@@@@@@  @@@@@@@   @@@@@@@@  @@@  @@@  
            @@!  @@@  !@@       !@@       @@!  @@!  
            !@!  @!@  !@!       !@!       !@!  !@!  
            @!@!@!@!  !!@@!!    !@!       !!@  !!@  
            !!!@!!!!   !!@!!!   !!!       !!!  !!!  
            !!:  !!!       !:!  :!!       !!:  !!:  
            :!:  !:!      !:!   :!:       :!:  :!:  
            ::   :::  :::: ::    ::: :::   ::   ::  
            :   : :  :: : :     :: :: :  :    :     {Fore.CYAN}Created by Bearlim
            
            '''

        print(banner)
        print("\n1)Random ASCII Art\n2)Text to Art\n")
        answer1 = input()
        while answer1 not in ['1', '2', 'exit']:
            print("Type a valid option")
            answer1 = input()
        if answer1 == '1':
            return random()
        elif answer1 == '2':
            return textArt()
        elif answer1 == 'exit':
            sys.exit()
    except KeyboardInterrupt:
        print("\nExiting...")    
        sys.exit()

def random():
    try:
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')
        print("How many random ASCII art you want? Only numbers!\n")
        answer = int(input())
        for i in range(0, answer + 1):
            a = art.randart()
            print(a)
        input("Press enter to go to Homescreen")
        return start()
    except KeyboardInterrupt:
        print("\nExiting...")  
        sys.exit()
    
def textArt():
    try:
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')
        print("Type the texto to converto to an ASCII Art:  ")
        text = input()
        print("1)Small font\n2)Medium font\n3)Large font\n4)Xlarge")       
        answer = input()
        while answer not in ['1', '2', '3', '4']:
            print("Type a valid option")
            answer = input()
        if answer == '1':
            weight = 'rnd-small'
        elif answer == '2':
            weight = 'rnd-medium'
        elif answer == '3':
            weight = 'rnd-large'
        elif answer == '4':
            weight = 'rnd-xlarge'
        art.tprint(text, font=weight)
        print("Do you want to test an another font?[y/n]")
        answer1 = input()
        while answer1 not in ['y', 'n']:
            print("Type a valid option")
            answer1 = input()
        while answer1 == 'y':
            art.tprint(text, font=weight)
            answer1 = input("Do you want to test an another font?[y/n]")
        if answer1 == 'n':
            return start()
    except KeyboardInterrupt:
        print("\nExiting...")    
        sys.exit()

start()

"""
################################################################
#####################  CREATED BY BEARLIM  #####################
################################################################
"""
