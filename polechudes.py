#!/usr/bin/python3
a = "kasparov"
new_string = ''
tmp = str(len(a) * '*')

def game_process(tmp, a, new_string):
	print('who is 13rd chess world champion\n')
	print(tmp)
	while tmp != a:
		letter = input("Enter a alpha\n")
		letter = letter.lower()
		for i in range(len(a)):
			if a[i] == letter:
				new_string += letter
			else:	
				new_string += tmp[i]
		tmp = new_string
		new_string = ''
		print(tmp)		
	print("You win!!!  13 chess world champion is: " + str(a))

def main():
	game_process(tmp, a, new_string)


if __name__ == '__main__':
	main()
