import random

def main():
	dificulity = input("what dificulity whould you like? write e for:easy-m for:meduim and h for:hard ")
	while dificulity not in ["h","e","m"]:
		dificulity = input("enter valid dificulity ")

	if dificulity == "e":
			secret_guess = random.randint(1,25)
		 
	elif dificulity == "m":
		secret_guess = random.randint(1,50)
	elif dificulity == "h":
		secret_guess = random.randint(1,100)

		
	guessed = None
	attempt = 0
	while guessed != secret_guess:
		guessed = input("guess the number bud ")
		
		if guessed.lower() == "quit":
			exit()
			return
		
		try:
			guessed = int(guessed)
			
			
		except ValueError:
			print("enter a number fucko or exit with word: quit ")
			continue
		attempt +=1
		
		guessed = int(guessed)
		if guessed == secret_guess:
			print(f"you guessed it in {attempt} !")
		elif guessed > secret_guess:
			print("nah too high")
			
		else:
			print("damn too low")
		
	
	
while True:
	main()
		
	play = input("wana play again? type y/n ")
	if play !="y":
		break
	 	

