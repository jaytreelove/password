import random


def strong_password(length):
	characters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ\
abcdefghijklmnopqrstuvwxyz\
1234567890!@#$%&*-")

	password = ''.join(random.choice(characters) for i in range(length))
	print (length, "characters: ", password)


while True:
	menu = input("\nEnter P for Password or Q to Quit: ")
	if menu.lower() == "q":
		break
	elif menu.lower() == "p":
		try:
			user_choice = int(input("\nEnter Password Character Length: "))

			strong_password(user_choice)
			print("\nOther password options:")
			strong_password(16)
			strong_password(20)
			strong_password(24)

		except:
			print("\nPlease enter a number.")

	else:
		print("\nMind your P's and Q's.")
