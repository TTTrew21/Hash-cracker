import hashlib
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess(dictionary, target_hash, hash_func):
    print("Trying...")
    for index, word in enumerate(dictionary):
        hashed_string = hash_func(word.encode()).hexdigest()
        if hashed_string == target_hash:
            print(f'{hashed_string}/{index}/{word}/True')
            print(f'{bcolors.OK}{bcolors.BOLD}Success.{bcolors.RESET}')
            return True, hashed_string
    print(f'{bcolors.FAIL}{bcolors.BOLD}Failed.{bcolors.RESET}')
    return False, target_hash

def load_password_file(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except UnicodeDecodeError:
        print(f"{bcolors.FAIL}Error: File encoding is not UTF-8. Please provide a UTF-8 encoded file.{bcolors.RESET}")
        return None
    except FileNotFoundError:
        print(f"{bcolors.FAIL}Error: File not found. Please provide a valid file path.{bcolors.RESET}")
        return None

def main_round():
    clear_screen()
    print(
        f"""{bcolors.OKCYAN}{bcolors.BOLD}
            |    Welcome     |
            | last 2024/5/31 |
            |    by haiaka   |
        {bcolors.RESET}"""
    )
    
    # Get the target hash and hash type from the user
    target_hash = input(f"{bcolors.WARNING}{bcolors.BOLD}target hash: {bcolors.RESET}").strip().lower()
    hash_type = input(f"{bcolors.WARNING}{bcolors.BOLD}hash type (md5, sha1, sha224, sha256, sha384, sha512a): {bcolors.RESET}").strip().lower()
    
    # Mapping user input to hashlib functions
    hash_funcs = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512
    }
    
    if hash_type not in hash_funcs:
        print(f"{bcolors.FAIL}Error: Unsupported hash type. Supported types are: {', '.join(hash_funcs.keys())}.{bcolors.RESET}")
        return
    
    hash_func = hash_funcs[hash_type]

    clear_screen()
    file_path = input("Password file: ").strip()
    dictionary = load_password_file(file_path)
    if dictionary is None:
        return
    
    input(f"{bcolors.WARNING}Press Enter to start attack.{bcolors.RESET}")
    clear_screen()
    success, hashed_string = guess(dictionary, target_hash, hash_func)

    while True:
        choice = input("[0]exit\n[1]try again\n")
        if choice == '0':
            sys.exit()
        elif choice == '1':
            main_round()
        else:
            print("Invalid choice. Please select [0] or [1].")

if __name__ == "__main__":
    main_round()
