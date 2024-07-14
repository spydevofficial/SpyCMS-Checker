import os
import requests
from multiprocessing import Pool
import colorama
from colorama import Fore, Style
import platform


def screen_clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
        os.system('color a')

colorama.init()

fg = [
    '\033[91;1m',  # red 0
    '\033[92;1m',  # green 1
    '\033[93;1m',  # yellow 2
    '\033[94;1m',  # blue 3
    '\033[95;1m',  # magenta 4
    '\033[96;1m',  # cyan 5
    '\033[97;1m'  # white 6
]

bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

os.makedirs("Results", exist_ok=True)


def laravelcheck(star):
    if "://" in star:
        star = star
    else:
        star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/.env"
    check = requests.get(url, headers=headers, timeout=3)
    resp = check.text
    try:
        if "DB_HOST" in resp:
            print(f"{gr}[+] Laravel CMS{res} => {star}\n")
            with open("Results/Laravel.txt", "a") as mrigel:
                mrigel.write(f'{star}\n')
        else:
            print(f"{red}[-] No CMS Found{res} => {star}\n")
    except:
        pass


def wpcheck(star):
    if "://" in star:
        star = star
    else:
        star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/wp-content/"
    check = requests.get(url, headers=headers, timeout=3)
    try:
        if check.status_code == 200:
            print(f"{gr}[+] Wordpress CMS{res} => {star}\n")
            with open("Results/Wordpress.txt", "a") as mrigel:
                mrigel.write(f'{star}\n')
        else:
            print(f"{red}[-] No CMS Found{res} => {star}\n")
    except:
        pass


def filter(star):
    try:
        laravelcheck(star)
        wpcheck(star)
    except:
        pass


def main():
    print('''            
            {0}  _____              _____ __  __  _____ 
            {1} / ____|            / ____|  \/  |/ ____|
            {1}| (___  _ __  _   _| |    | \\  / | (___  
            {2} \\___ \\| '_ \\| | | | |    | |\\/| | \\___ \\ 
            {2} ____) | |_) | |_| | |____| |  | |____) |
            {3}|_____/| .__/ \\__, |\\_____|_|  |_|_____/ 
            {3}       | |     __/ |                     
            {0}       |_|    |___/       channel : @spydev_channel                                             
           {2}\\━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━/
           \t├╼ {3}BY : spydev{2}
           \t└╼ {3}Laravel & Wordpress CMS Checker
        \033[0m'''.format(fg[1], fg[0], fg[5], fg[3]))
    list = input(f"[+]{gr}Give Me Your List/{red}pydev> {gr}${res} ")
    star = open(list, 'r').readlines()
    try:
        ThreadPool = Pool(50)
        ThreadPool.map(filter, star)
        ThreadPool.close()
        ThreadPool.join()
    except:
        pass


if __name__ == '__main__':
    screen_clear()
    main()
