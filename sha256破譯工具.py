import hashlib
import os

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

os.system('cls')
ans = str.lower(input(f"{bcolors.WARNING}{bcolors.BOLD}target(SHA256):{bcolors.RESET}"))
setting = str.lower(input("Disable sha256. (y/n)"))

d = []

os.system('cls')
f=input("Password file:")
with open(str(f), mode='r') as file:
	d = [line.strip() for line in file.readlines()]

def guess():
	s = 'false'

	for i in range(0, len(d)):

		hashed_string = hashlib.sha256(d[i].encode()).hexdigest()
        
		if hashed_string == ans:
			s = 'true'
		if setting == "y":
			print(f'Disabled/{d[i]}/{s}')
		else: print(f'{hashed_string}/{d[i]}/{s}')

		if s == 'true':
			break
	if s == 'true':
		print(f'{bcolors.OK}{bcolors.BOLD}Attack successful.{bcolors.RESET}')
		return
	print(f'{bcolors.FAIL}{bcolors.BOLD}Attack failed.{bcolors.RESET}')

i = input(f"{bcolors.WARNING}Enter to start attack.{bcolors.RESET}")
os.system('cls')
guess()	