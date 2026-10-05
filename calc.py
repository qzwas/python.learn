def add(a,b):
	c=a+b
	return c
def mul(a,b):
	c=a*b
	return c
def minus(a,b):
	c=a-b
	return c
def div(a,b):
	c=a/b
	return c

def main():
	print("=== this is a Calcolator what do you wana calc? add-mul-minus-div ===")
	
	user_type = input("enter type: ")
	if user_type == "quit":
		quit()	
	while user_type not in ["add","mul","minus","div"]:
		user_type = input("enter a valid type ")
	
	while True:
		
			try:
				a = int(input("what is the first number?:  "))
				b = int(input("what is the second number?:  "))
			except ValueError:
				print("enter a valid number")
				continue
			if user_type == "add":
				result = add(a,b)
				print(result)
				break
				
			elif user_type == "minus":
				result = minus(a,b)
				print(result)
				break
				
			elif user_type == "mul":
				result = mul(a,b)
				print(result)
				break
			
			elif user_type == "div":
				try:
					result = div(a,b)
					print(result)
					break
				except ZeroDivisionError:
					print("you cant divide by 0")
					
while True:
	main()
	again = input("more or nah? y/n ")
	if again != "y":
		break
			
