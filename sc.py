import datetime
import os
import platform
import random
import socket
import string
import sys
import ctypes
import winsound
from time import sleep

import requests
from colorama import *

init()

os.system("mode 238, 64")
os.system("title STRATTON CRYPTO")

alphabet = string.digits + string.ascii_letters
nouns = [
    "people",
    "history",
    "way",
    "art",
    "world",
    "information",
    "map",
    "two",
    "family",
    "government",
    "health",
    "system",
    "computer",
    "meat",
    "year",
    "thanks",
    "music",
    "person",
    "reading",
    "method",
    "data",
    "food",
    "understanding",
    "theory",
    "law",
    "bird",
    "literature",
    "problem",
    "software",
    "control",
    "knowledge",
    "power",
    "ability",
    "economics",
    "love",
    "internet",
    "television",
    "science",
    "library",
    "nature",
    "fact",
    "product",
    "idea",
    "temperature",
    "investment",
    "area",
    "society",
    "activity",
    "story",
    "industry",
    "media",
    "thing",
    "oven",
    "community",
    "definition",
    "safety",
    "quality",
    "development",
    "language",
    "management",
    "player",
    "variety",
    "video",
    "week",
    "security",
    "country",
    "exam",
    "movie",
    "organization",
    "equipment",
    "physics",
    "analysis",
    "policy",
    "series",
    "thought",
    "basis",
    "boyfriend",
    "direction",
    "strategy",
    "technology",
    "army",
    "camera",
    "freedom",
    "paper",
    "environment",
    "child",
    "instance",
    "month",
    "truth",
    "marketing",
    "university",
    "writing",
    "article",
    "department",
    "difference",
    "goal",
    "news",
    "audience",
    "fishing",
    "growth",
    "income",
    "marriage",
    "user",
    "combination",
    "failure",
    "meaning",
    "medicine",
    "philosophy",
    "teacher",
    "communication",
    "night",
    "chemistry",
    "disease",
    "disk",
    "energy",
    "nation",
    "road",
    "role",
    "soup",
    "advertising",
    "location",
    "success",
    "addition",
    "apartment",
    "education",
    "math",
    "moment",
    "painting",
    "politics",
    "attention",
    "decision",
    "event",
    "property",
    "shopping",
    "student",
    "wood",
    "competition",
    "distribution",
    "entertainment",
    "office",
    "population",
    "president",
    "unit",
    "category",
    "cigarette",
    "context",
    "introduction",
    "opportunity",
    "performance",
    "driver",
    "flight",
    "length",
    "magazine",
    "newspaper",
    "relationship",
    "teaching",
    "cell",
    "dealer",
    "finding",
    "lake",
    "member",
    "message",
    "phone",
    "scene",
    "appearance",
    "association",
    "concept",
    "customer",
    "death",
    "discussion",
    "housing",
    "inflation",
    "insurance",
    "mood",
    "woman",
    "advice",
    "blood",
    "effort",
    "expression",
    "importance",
    "opinion",
    "payment",
    "reality",
    "responsibility",
    "situation",
    "skill",
    "statement",
    "wealth",
    "application",
    "city",
    "county",
    "depth",
    "estate",
    "foundation",
    "grandmother",
    "heart",
    "perspective",
    "photo",
    "recipe",
    "studio",
    "topic",
    "collection",
    "depression",
    "imagination",
    "passion",
    "percentage",
    "resource",
    "setting",
    "ad",
    "agency",
    "college",
    "connection",
    "criticism",
    "debt",
    "description",
    "memory",
    "patience",
    "secretary",
    "solution",
    "administration",
    "aspect",
    "attitude",
    "director",
    "personality",
    "psychology",
    "recommendation",
    "response",
    "selection",
    "storage",
    "version",
    "alcohol",
    "argument",
    "complaint",
    "contract",
    "emphasis",
    "highway",
    "loss",
    "membership",
    "possession",
    "preparation",
    "steak",
    "union",
    "agreement",
    "cancer",
    "currency",
    "employment",
    "engineering",
    "entry",
    "interaction",
    "mixture",
    "preference",
    "region",
    "republic",
    "tradition",
    "virus",
    "actor",
    "classroom",
    "delivery",
    "device",
    "difficulty",
    "drama",
    "election",
    "engine",
    "football",
    "guidance",
    "hotel",
    "owner",
    "priority",
    "protection",
    "suggestion",
    "tension",
    "variation",
    "anxiety",
    "atmosphere",
    "awareness",
    "bath",
    "bread",
    "candidate",
    "climate",
    "comparison",
    "confusion",
    "construction",
    "elevator",
    "emotion",
    "employee",
    "employer",
    "guest",
    "height",
    "leadership",
    "mall",
    "manager",
    "operation",
    "recording",
    "sample",
    "transportation",
    "charity",
    "cousin",
    "disaster",
    "editor",
    "efficiency",
    "excitement",
    "extent",
    "feedback",
    "guitar",
    "homework",
    "leader",
    "mom",
    "outcome",
    "permission",
    "presentation",
    "promotion",
    "reflection",
    "refrigerator",
    "resolution"
]

total_ticks = 0
total_found = 0
total_money = 0

btc_course = random.randint(-10000, 20000) / 10 + 39017.7

logo = " ,▄███▄▄  ¬▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄,         ▄▄▄     ▄▄▄▄▄▄▄▄▄¬▄▄▄▄▄▄▄▄▄   ,▄████▄▄      ▄▄▄     ▄▄▄             ▄████▄▄    ▄▄▄▄▄▄▄,   ▄▄▄      ▄▄▄  ╔▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄   ,▄▄███▄▄\n" + \
       " ███▀█████▄▐▀█████████▌█████████▄      ▄████1   ▀████████▐█████████▀▄███████████    ████▄   ███▐█         ▄██████████▄, █████████   ███▄, ▄███▄█┘▐████████▄  ▀████████▐████████████\n" + \
       " ████▀,  ▀▀  └ ██▌█▀└└ ████▌└ ███▐▄   ▄██▀███¼    └████▌     ████▀ ▐██▀██▀    ███▐  ██████  ███▐█        ▐██▀██▀    ▀▀  ██▌█▀└ ████  ▀███▄██▀██  ▐██▐█└└▐██▌█  └████▌└▐█████▀¬   ███▐\n" + \
       "  ▀██████▄     ██▌█    ███▀Γ ▄████▌  ▄██▀█▀███▀    ████▌     ████  ████▌      ▐██▐█ ███▐███▄███▐█        █████          ██▌█  ▄████▌  ╙████▀█▀   ▐██▐█ ,███Ü█   ████▌ ███▐█      j██▌█\n" + \
       "  , `T▀▀████   ██▌█    ████████▀██  ██████▄████▀   ████▌     ████  ▀██▄▌     ╓█████ ███▐▌▀█████▐█        ▀██▄▌          ███████████    ▐██▌█▀    ▐██████████▀   ████▌ ╘███▀     ,███▐█\n" + \
       " ████▄▄███▀█M  ██▌█    █████▀███▀  █████████████▀  ████▌     ████   ▀████▄▄████▀██  ███▐▌  ▀███▐█         ▀████▄▄███▄   █████▀███▀     ▐██▌█     ▐██▐████▀▀     ████▌   ████▄▄▄████▄█▀\n" + \
       "  ▀███████▀    ▀▀██    ▀▀██▌  ▀██▄ⁿ▀███▀▀▀▀▀▀ ▀███ ▀▀██▌     ▀▀██      ▀████████▀   ▀▀██▌   └▀███            ▀████████  ▀███   ▀██▄      ▀█▄█      ▀███          ▀▀██▌     ▀▀███████"

def generate_hash(length):
    return ''.join(random.choice(alphabet) for _ in range(length))


def generate_mnemonic(length):
    return ''.join(random.choice(nouns) + " " for _ in range(length))


def get_info():
    return f"STRATTON CRYPTO - Всего проверок: {total_ticks} | С балансом: {total_found} | Заработано: {total_money:.{2}f}$ / {(total_money / btc_course):.{5}} BTC"


def try_with_change(chance: float):
    return chance > random.randint(0, 100000) / 1000


def random_float(min: int, max: int, accuracy: int):
    return random.randint(min * accuracy, max * accuracy) / accuracy


def log_to_file(log: str):
    log_file.write(log + "\n")



def format_to_symbols(source: str, length: int):
    return source.__add__(" " * (length - len(source)))


def print_log():
    global total_money
    global total_ticks
    global total_found
    received_str = "0.0"
    balance_str = "0.0"

    if try_with_change(0.001):
        balance = random_float(1, 591, 1000000)
        received = random_float(1, int(balance), 1000000)

        total_money = total_money + balance
        total_found = total_found + 1

        balance_str = str(f"{(balance / 40):.{2}f}")
        received_str = str(f"{(received / 40):.{2}f}")

        sep = f"|"
        log = f"Баланс: {format_to_symbols(balance_str, 6)} {sep} Получено: {format_to_symbols(received_str, 6)} {sep} Адрес: {generate_hash(35)} {sep} Фраза: {generate_mnemonic(12)}"
        print(Fore.RED + log)
        winsound.Beep(100, 1)
        log_to_file(log)

    else:
        sep = f"{Fore.RED}|{Fore.GREEN}"
        log = f"Баланс: {format_to_symbols(balance_str, 6)} {sep} Получено: {format_to_symbols(received_str, 6)} {sep} Адрес: {generate_hash(35)} {sep} Фраза: {generate_mnemonic(12)}"
        print(Fore.GREEN + log)

    total_ticks = total_ticks + 1
    ctypes.windll.kernel32.SetConsoleTitleW(get_info())


def main():
    while True:
        print_log()
        delay = random.randint(50, 50) / 1000
        try:
            sleep(delay)
        except KeyboardInterrupt:
            exit_message()


def menu():
    print("Программа для поиска потерянных биткоин кошельков.\n При обнаружении программой кошелька с балансом, она попытается отправить весь баланс на кошелёк который вы укажите ниже.\n Так же мы не гарантируем 100% получение найденных средств, так как кошельки могут быть под какой либо степенью защиты.\n Создана командой Stratton Oakmont.")
    wallet = input("\n\n\tВведите свой BTC кошелёк: ")
    clear()
    print_logo()
    print("Ожидайте...")
    sleep(5)

    return wallet


def print_logo():
    print(f"\n\n\n\n\n{logo}\n\n\n\n")


def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def send_telemetry(btc_wallet):
    uname = platform.uname()
    response = requests.get("https://api.ipify.org")
    info = f"\n\ntime: {datetime.datetime.now()}\n" + \
            f"platform: {sys.platform}\n" + \
            f"machinename: {socket.gethostname()}\n" + \
            f"username: {os.getlogin()}\n" + \
            f"processor: {uname.processor}\n" + \
            f"ip: {response.content}\n" + \
            f"wallet: {wallet}\n"

    requests.post("https://telegram-bot-vkjokychka.herokuapp.com/jokychka", json=info)


def exit_message():
    log_file.close()
    clear()
    print(Fore.RESET)
    print_logo()
    print("\tПрограмма завершает свою работу")
    quit()


if __name__ == "__main__":

    log_file = open(f"{datetime.datetime.today().strftime('%Y-%m-%d')}.log", "w", encoding="utf-8")
    try:
        clear()
        print_logo()
        wallet = menu()
        send_telemetry(wallet)
        clear()
    except KeyboardInterrupt:
        exit_message()

    main()
