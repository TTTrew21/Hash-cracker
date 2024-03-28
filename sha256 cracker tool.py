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



def guess(d, ans, setting):
	s = False

	for i in range(0, len(d)):

		hashed_string = hashlib.sha256(d[i].encode()).hexdigest()

		if hashed_string == ans:
			s = True
			break
		if setting == "y":
			print(f'Disabled/{d[i]}/{s}')
		else:
			print(f'{hashed_string}/{d[i]}/{s}')
		
	if s:
		print(f'{bcolors.OK}{bcolors.BOLD}Attack successful.{bcolors.RESET}')
		return True, hashed_string

	print(f'{bcolors.FAIL}{bcolors.BOLD}Attack failed.{bcolors.RESET}')
	return False, ans

def round():
	os.system('cls')
	ans = str.lower(input(f"{bcolors.WARNING}{bcolors.BOLD}target(SHA256):{bcolors.RESET}"))
	setting = str.lower(input("Disable sha256. (y/n)"))

	dic = []

	os.system('cls')
	f = input("Password file:")
	with open(str(f), mode='r') as file:
		dic = [line.strip() for line in file.readlines()]

	i = input(f"{bcolors.WARNING}Enter to start attack.{bcolors.RESET}")
	os.system('cls')
	a, b = guess(dic, ans, setting)

	if a:
		def ques():
			n = int(input("[0]exit\n[1]print the sha256\n[2]try again\n"))
			if n == 0: exit()
			elif n == 1:
				print(b)
				ques()
			elif n == 2: round()
		ques()

round()
