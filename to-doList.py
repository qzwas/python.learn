tasks = []
def add(tasks):
	title = input("title: ")
	content = input("content ")
	tasks.append( 
	{
	"title": title,
	"content": content
	}
	)
	print(f"you added {tasks}")
def liste(tasks):
	if not tasks:
		print(" === you dont have any tasks === ")
	else:
		for task in tasks:
			print("===",task,"===")
		
def delete(tasks):
	user = input("what task do you wanna delete? ")
	for task in tasks:
		if task["title"] == user:
			tasks.remove(task)
			break
	
def main():
	
	print("======= add task , list tasks , delete tasks ======")
 
	
	user = input("")
	if user == "add":
		add(tasks)
	elif user == "delete":
		delete(tasks)
	elif user == "list":
		liste(tasks)
	elif user == "quit":
		quit()
	elif user == "q":
		quit()
	
	
while True:
	main()

