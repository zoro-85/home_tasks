#!/usr/bin/python3
import sys

display_list = [['1','2','3'], ['4','5','6'], ['7','8','9']]
d = {
	'1' : ['1','2','3'], 
	'2' : ['4','5','6'], 
	'3' : ['7','8','9']
    }
win_d = {
	'1' : ['1', '2', '3'], 
	'2' : ['4', '5', '6'], 
	'3' : ['7', '8', '9'], 
	'4' : ['1', '4', '7'], 
	'5' : ['8', '5', '2'], 
	'6' : ['9', '6', '3'], 
	'7' : ['7', '5', '3'], 
	'8' : ['9', '5', '1']
	}
team1 = []
team2 = []

#prints original 'display_list'
def show_display_list(display_list):
	for i in display_list:
		print(i)

#returns True if choosen element is existence in 'd'
def check_element_existence(d, element):
	for i in display_list:
		if element in i:
			return True
	return False

#returns element if choosen element is existence in 'd'
def check_choosen_number(d, team_number):
	global element
	name = 'Team' + team_number
	element = input(name + ': choose number\n')
	while check_element_existence(d, element) == False:
		element = input(name + ': choose number from list\n')
	return element

# changes 'display_list' symbol and print 
# changed 'display_list'
def show_changed_display(display_list, element, symbol):
	for i in display_list:
		if element in i:
			i[i.index(element)] = symbol
		print(i)

#create new 'team' list by 'd' keys
def create_team_list(win_d,team, element):
	for i, j in win_d.items():
		if element in j:
			team.append(i)

#check game winner 
def check_winner(team, team_number):
	for i in team:
		if team.count(i) == 3:
			print('TEAM'+ team_number + '  WIN!!!')
			sys.exit()

#game procces 
def game_process(display_list, d, team, team_number, symbol):
	check_choosen_number(d, team_number)
	show_changed_display(display_list, element, symbol)
	create_team_list(win_d,team, element)
	check_winner(team, team_number)


def main():
	show_display_list(display_list)
	x = 0
	while x < 5:
		game_process(display_list, d, team1, '1', 'X')
		x += 1
		if x == 5:
			sys.exit('Game ended with DRAW!!!')
		game_process(display_list, d, team2, '2', 'O')


if __name__ == '__main__':
	main()
