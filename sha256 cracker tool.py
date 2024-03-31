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



def guess(d, ans):
	s = False

	print("Trying...")

	for i in d:

		hashed_string = hashlib.sha256(i.encode()).hexdigest()

		if hashed_string == ans:
			s = True
			print(f'{hashed_string}/{i}/{s}')
			break
			
	if s:
		print(f'{bcolors.OK}{bcolors.BOLD}Attack successful.{bcolors.RESET}')
		return True, hashed_string

	print(f'{bcolors.FAIL}{bcolors.BOLD}Attack failed.{bcolors.RESET}')
	return False, ans

def round():
	os.system('cls')
	print(
	f"""{bcolors.OKCYAN}{bcolors.BOLD}
		|    Welcome     |
		| last 2024/3/21 |
		|    by Jeff3300 |
	{bcolors.RESET}""")
	ans = str.lower(input(f"{bcolors.WARNING}{bcolors.BOLD}target(SHA256):{bcolors.RESET}"))

	dic = []

	os.system('cls')

	f = input("Password file:")
	with open(str(f), mode='r') as file:
		dic = [line.strip() for line in file.readlines()]

	i = input(f"{bcolors.WARNING}Enter to start attack.{bcolors.RESET}")
	os.system('cls')
	a, b = guess(dic, ans)

	def ques():
		n = int(input("[0]exit\n[1]try again\n"))
		if n == 0: exit()
		elif n ==1: round()
	ques()

round()
	
