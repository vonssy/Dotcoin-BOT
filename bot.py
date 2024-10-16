import requests
import json
import os
from colorama import *
from datetime import datetime, timedelta
from dateutil import parser
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Dotcoin:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Profile': 'public',
            'Apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
            'Cache-Control': 'no-cache',
            'Host': 'api.dotcoin.bot',
            'Origin': 'https://app.dotcoin.bot',
            'Pragma': 'no-cache',
            'Referer': 'https://app.dotcoin.bot/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Dotcoin - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        
    def get_token(self, query: str, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/functions/v1/getToken'
        data = json.dumps({'initData': query})
        self.headers.update({
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result['token']
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def user_info(self, token: str, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/get_user_info'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def assets_info(self, token: str, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/get_assets'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def spinner(self, token: str, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/spin'
        data = json.dumps({})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def double_coins(self, token: str, coins: int, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/try_your_luck'
        data = json.dumps({'coins': coins})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def save_coins(self, token: str, taps: int, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/save_coins'
        data = json.dumps({'coins': taps})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def restore_attempts(self, token: str, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/restore_attempt'
        data = json.dumps({})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def upgrade_multitap(self, token: str, level: int, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/add_multitap'
        data = json.dumps({'lvl': level})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def upgrade_attempts(self, token: str, level: int, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/add_attempts'
        data = json.dumps({'lvl': level})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def upgrade_dtc_miner(self, token: str, user_id: int, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/functions/v1/upgradeDTCMiner'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Length': '0',
            'Content-Type': 'application/json',
            'X-Telegram-User-Id': str(user_id)
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None

    def dtc_miner_rate(self, miner_level: int) -> str:
        if miner_level == 0:
            return 0
        return 2 ** miner_level
    
    def tasks(self, token: str, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/get_filtered_tasks'
        data = json.dumps({"platform":"tdesktop","locale":"en","is_premium":False})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def complete_tasks(self, token: str, task_id: int, retries=3, delay=2):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/complete_task'
        data = json.dumps({'oid': task_id})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if response.status_code == 200:
                    return result
                else:
                    return None
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def question(self):
        while True:
            multitap_upgrade = input("Upgrade Multitap Level? [y/n] -> ").strip().lower()
            if multitap_upgrade in ["y", "n"]:
                multitap_upgrade = multitap_upgrade == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
        multitap_count = 0
        if multitap_upgrade:
            while True:
                try:
                    multitap_count = int(input("How many times? -> "))
                    if multitap_count > 0:
                        break
                    else:
                        print(f"{Fore.RED+Style.BRIGHT}Please enter a positive number.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED+Style.BRIGHT}Invalid input. Enter a number.{Style.RESET_ALL}")
        
        while True:
            attempts_upgrade = input("Upgrade Limit Attempts? [y/n] -> ").strip().lower()
            if attempts_upgrade in ["y", "n"]:
                attempts_upgrade = attempts_upgrade == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
        attempts_count = 0
        if attempts_upgrade:
            while True:
                try:
                    attempts_count = int(input("How many times? -> "))
                    if attempts_count > 0:
                        break
                    else:
                        print(f"{Fore.RED+Style.BRIGHT}Please enter a positive number.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED+Style.BRIGHT}Invalid input. Enter a number.{Style.RESET_ALL}")

        while True:
            miner_upgrade = input("Upgarde DTC Mining Level? [y/n] -> ").strip().lower()
            if miner_upgrade in ["y", "n"]:
                miner_upgrade = miner_upgrade == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")

        while True:
            go_spin = input("Play Game Spinner? [y/n] -> ").strip().lower()
            if go_spin in ["y", "n"]:
                go_spin = go_spin == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to play or 'n' to skip.{Style.RESET_ALL}")

        while True:
            go_task = input("Check Available Tasks? [y/n] -> ").strip().lower()
            if go_task in ["y", "n"]:
                go_task = go_task == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to check or 'n' to skip.{Style.RESET_ALL}")

        return multitap_upgrade, multitap_count, attempts_upgrade, attempts_count, miner_upgrade, go_spin, go_task
    
    def process_query(self, query: str, add_multitap: bool, multitap_count: int, add_attempts: bool, attempts_count: int, dtc_miner: bool, spinner: bool, check_task: bool):

        token = self.get_token(query)

        if token:
            user = self.user_info(token)
            if user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['first_name']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['balance']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}Point ] [ Level{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['level']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Booster Info ]{Style.RESET_ALL}")
                time.sleep(1)
                miner_level = user['dtc_level']
                dtc_rate = self.dtc_miner_rate(miner_level)
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Multitap Level   : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}{user['multiple_clicks']}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Daily Attempts   : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}{user['limit_attempts']}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining Level : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}{miner_level}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining Rate  : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}{dtc_rate} $DTC/Day{Style.RESET_ALL}"
                )
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Assets Info ]{Style.RESET_ALL}")
                time.sleep(1)
                assets = self.assets_info(token)
                if assets:
                    for asset in assets:

                        if asset['symbol'] == 'VENOM':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Venom Amount     : {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{asset['amount']} ${asset['symbol']}{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Dotcoin Amount   : {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{asset['amount']} ${asset['symbol']}{Style.RESET_ALL}"
                            )
                else:
                    self.log(f"{Fore.RED+Style.BRIGHT}[ Assets Info ] None{Style.RESET_ALL}")
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Upgrade Boost ]{Style.RESET_ALL}")
                time.sleep(1)
                if add_multitap:
                    for i in range(multitap_count):
                        user = self.user_info(token)
                        multitap_level = user['multiple_clicks']
                        upgrade = self.upgrade_multitap(token, multitap_level)
                        if upgrade['success']:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Multitap         : {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Upgrade Success{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}Level {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{multitap_level + 1}{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Multitap         : {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Not Enough Balance{Style.RESET_ALL}"
                            )
                            break
                        time.sleep(1)
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Multitap         : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Upgrade Boost ]{Style.RESET_ALL}")
                time.sleep(1)
                if add_attempts:
                    for i in range(attempts_count):
                        user = self.user_info(token)
                        attempts_level = user['limit_attempts'] - 9
                        upgrade = self.upgrade_attempts(token, attempts_level)
                        if upgrade['success']:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Limit Attempts   : {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Upgrade Success{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}Level {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{attempts_level + 1}{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Limit Attempts   : {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Not Enough Balance{Style.RESET_ALL}"
                            )
                            break
                        time.sleep(1)
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Limit Attempts   : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Upgrade Boost ]{Style.RESET_ALL}")
                time.sleep(1)
                if dtc_miner:
                    user = self.user_info(token)
                    user_id = user['id']
                    miner_level = user['dtc_level']
                    upgrade = self.upgrade_dtc_miner(token, user_id)
                    if upgrade['success']:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining       : {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT}Upgrade Success{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}Level {Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT}{miner_level + 1}{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining       : {Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT}Upgrade Failed{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining       : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

                if spinner:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT}Spinner{Style.RESET_ALL}"
                    )
                    time.sleep(1)

                    assets = self.assets_info(token)
                    for asset in assets:
                        if asset['symbol'] == 'DTC':
                            dtc_amount = asset['amount']

                            if dtc_amount >= 5:

                                spinner_time = parser.isoparse(user['spin_updated_at'])
                                spinner_time_wib = spinner_time.astimezone(wib)
                                spinner_ready = (spinner_time_wib + timedelta(hours=8)).strftime('%x %X %Z')

                                spin = self.spinner(token)
                                if spin['success']:
                                    if spin['symbol'] == 'VENOM':
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT}Success{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT}{spin['amount']} $VENOM{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT}Success{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT}{spin['amount']} $DTC{Style.RESET_ALL}"
                                        )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Already Play Spinner{Style.RESET_ALL}"
                                    )
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Comeback at {Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT}{spinner_ready}{Style.RESET_ALL}"
                                    )
                                time.sleep(1)
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}Not Enough DTC{Style.RESET_ALL}"
                                )
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Amount  : {Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT}{dtc_amount} $DTC{Style.RESET_ALL}"
                                )
                else:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Spinner Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

                self.log(
                    f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}Double Coins{Style.RESET_ALL}"
                )
                time.sleep(1)
                if user['gamex2_times'] != 0:
                    coins = 150000
                    gacha = self.double_coins(token, coins)
                    if gacha['success']:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Gacha   : {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT}WIN{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT}{coins}{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Gacha   : {Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT}LOSE{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Gacha   : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Already Gacha Today{Style.RESET_ALL}"
                    )
                time.sleep(1)

                self.log(
                    f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}Tap Tap{Style.RESET_ALL}"
                )
                time.sleep(1)
                energy = user['daily_attempts']
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}Energy {energy}{Style.RESET_ALL}"
                )
                time.sleep(1)
                while energy > 0:
                    for _ in range(energy):
                        time.sleep(3)
                        taps = self.save_coins(token, 20000)
                        if taps['success']:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Success{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Failed{Style.RESET_ALL}"
                            )
                    user = self.user_info(token)
                    energy = user['daily_attempts']
                    if energy == 0:
                        count = 0
                        while count < 1:
                            restore = self.restore_attempts(token)
                            if restore['success'] and restore:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Restore Energy Success{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}Restore Energy Reached Limit{Style.RESET_ALL}"
                                )
                                count += 1
                            time.sleep(1)
                            user = self.user_info(token)
                            energy = user['daily_attempts']
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Energy has Run Out{Style.RESET_ALL}"
                    )
                time.sleep(1)

                if check_task:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Check Task ] {Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT}Checked{Style.RESET_ALL}"
                    )
                    tasks = self.tasks(token)
                    if tasks:
                        for task in tasks:
                            task_id = task['id']

                            if task['is_completed'] is None:

                                complete = self.complete_tasks(token, task_id)
                                if complete['success']:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Completed{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT}{task['reward']}{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT}Not Completed{Style.RESET_ALL}"
                                    )
                                time.sleep(1)
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Task{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT}Failed to Checked Tasks{Style.RESET_ALL}"
                        )
                    time.sleep(1)
                else:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Check Task ] {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

            else:
                self.log(f"{Fore.RED+Style.BRIGHT}[ Account None ]{Style.RESET_ALL}")
                time.sleep(1)

        else:
            self.log(f"{Fore.RED+Style.BRIGHT}[ Token None ]{Style.RESET_ALL}")
            time.sleep(1)
        
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            add_multitap, multitap_count, add_attempts, attempts_count, dtc_miner, spinner, check_task = self.question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, add_multitap, multitap_count, add_attempts, attempts_count, dtc_miner, spinner, check_task)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Dotcoin - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    dotcoin = Dotcoin()
    dotcoin.main()