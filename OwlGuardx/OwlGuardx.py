import hashlib
import requests
import sys
import time
import os
import colorama
from colorama import Fore
import itertools
import threading

colorama.init(autoreset=False)  # Colors persist across prints

ASCII_ART = r"""{}
   ___           _  ____                     _       
  / _ \__      _| |/ ___|_   _  __ _ _ __ __| |_  __ 
 | | | \ \ /\ / / | |  _| | | |/ _` | '__/ _` \ \/ / 
 | |_| |\ V  V /| | |_| | |_| | (_| | | | (_| |>  <  
  \___/  \_/\_/ |_|\____|\__,_|\__,_|_|  \__,_/_/\_\ 
                                                     
""".format(Fore.GREEN)

MENU_TEXT = f"""{Fore.YELLOW}
[1] Check if a password has been leaked
[2] Exit
"""

stop_spinner = False
start_time = None  # Track animation start time

def spinning_cursor():
    """Loading animation (spinning slash) for at least 3 seconds."""
    global stop_spinner, start_time
    start_time = time.time()
    
    for cursor in itertools.cycle(["|", "/", "-", "\\"]):
        if stop_spinner and time.time() - start_time >= 3:  # Min 3 seconds
            break
        sys.stdout.write(Fore.BLUE + f"\rChecking... {cursor} ")
        sys.stdout.flush()
        time.sleep(0.1)
    
    sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the line after animation

def check_password_pwned(password):
    """Checks if a password has been leaked."""
    global stop_spinner
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    # Start loading animation
    stop_spinner = False
    spinner_thread = threading.Thread(target=spinning_cursor)
    spinner_thread.start()

    response = requests.get(url)

    # Ensure animation runs for at least 3 seconds
    while time.time() - start_time < 3:
        time.sleep(0.1)

    # Stop animation
    stop_spinner = True
    spinner_thread.join()

    if response.status_code != 200:
        print(Fore.RED + "\nError connecting to API!")
        return
    
    hashes = response.text.splitlines()
    for line in hashes:
        leaked_hash, count = line.split(":")
        if leaked_hash == suffix:
            print(Fore.RED + f"\n⚠️  This password has been found in {count} breaches!")
            print(Fore.RED + "🚨 This password has previously appeared in a data breach and should never be used.")
            print(Fore.RED + "🔄 If you've ever used it anywhere before, change it immediately!")
            input(Fore.YELLOW + "\nPress Enter to continue...")
            os.system("cls")  # Clear screen
            return
    
    print(Fore.GREEN + "\n✅ This password has NOT been found in any leaks.")
    input(Fore.YELLOW + "Press Enter to continue...")
    os.system("cls")  # Clear screen

def main():
    while True:
        os.system("cls")  # Clear screen before showing the menu
        print(ASCII_ART)
        print(MENU_TEXT)
        choice = input(Fore.CYAN + "Select an option: ")

        if choice == "1":
            password = input(Fore.MAGENTA + "Enter the password to check: ")
            check_password_pwned(password)
        elif choice == "2":
            print(Fore.YELLOW + "Exiting program...")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option, try again!")
            input(Fore.YELLOW + "Press Enter to continue...")
            os.system("cls")  # Clear screen

if __name__ == "__main__":
    main()
