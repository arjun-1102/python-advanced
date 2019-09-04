import sys

def rememberer(thing):
	with open("database.txt", "a") as file:
		file.write(thing+"\n")

def show():
	with open("database.txt", "r") as file:
		for line in file:
			print(line)

if __name__ == '__main__':
	if sys.argv[1].lower()=='--list':
		show()
	else:
		rememberer(' '.join(sys.argv[1:]))