#!/usr/bin/python3

def my_len(string):
	'''
	   Returns count of symbols in the string
		string: given string
	'''
	flag = 0
	for i in string:
		flag += 1
	return flag


def element_by_index(string, element):
	'''
	   Returns element's index in the string
		string: given string
		element: choosen element
	'''
	flag = 0
	for i in string:
		if i is element:
			return flag
		flag += 1

def element_count(string, element):
	'''
	   Returns count of choosen element
		string: given string
		element: choosen element
	'''
	flag = 0
	for i in string:
		if i is element:
			flag += 1
	return flag

def replace_element(string, old_element, new_element):
	'''
	   Returns new string with changed values
		string: given string
		old_element: wich will be changed in the string
		new_element: new value for the new string
	'''
	new_string = ''
	for i in string:	
		if i is old_element:
			new_string += new_element
		else:  	
			new_string += i
	return new_string

def string_islower(string):
	'''
	   Return True if all cased characters in String
	   are lowercase and there is at least one cased 
	   character in String, False otherwise
		string: given string
	'''
	if my_len(string) == 0:
		return False
	for i in string:
		if 'a' <= i <= 'z':
			continue
		else:
			return False
	return True

def string_isupper(string):
	'''
	   Return True if all cased characters in String
	   are uppercase and there is at least one 
	   cased character in String, False otherwise.
		string: given string
	'''
	if my_len(string) == 0:
		return False
	for i in string:
		if 'A' <= i <= 'Z':
			continue
		else:
			return False
	return True

def string_isdigit(string):
	'''
           Return True if all cased characters in String
           are number and there is at least one 
           cased character in String, False otherwise.
		string: given string
        '''
	numbers = '0123456789'
	if my_len(string) == 0:
		return False
	for i in string:
		if i in numbers:
			continue
		else:
			return False
	return True

def index_value(string, index):
	'''
	   Return the value of given index in the string
		string: given string
		index: choosen index
	'''
	flag = 0
	for i in string:
		if flag is index:
			return i
		flag += 1

def my_reverse(string):
	'''
	   Return string on the oposite side
		string: given string
	'''
	new_string = ''
	x = my_len(string)
	while x > 0:
		new_string += index_value(string, x - 1)
		x -= 1
	return new_string

def my_sss(string, start, stop, step = 1):
	new_string = ''
	while start < stop:
		new_string += index_value(string, start)
		start += step	
	return new_string

def my_capitalize(string):
	'''
	   Return a capitalized version of String, i.e. make the first character
    	   have upper case and the rest lower case. 
		string: given string
	'''
	new_string = ''
	i = 0
	while i < my_len(string):
		if i == 0:
			if string_islower(index_value(string, i)):
				new_string += chr(ord(index_value(string, i) ) - 32)
			else:
				 new_string += index_value(string, i)
		else:
			if string_islower(index_value(string, i)):
				new_string += index_value(string, i)
			else:
				new_string += chr(ord(index_value(string, i) ) + 32)
			
		i += 1
	return new_string

def my_lower(string):
	'''
	   Return a new String converted to lowercase.
		string: given string	
	'''
	new_string = ''
	for i in string:
		if string_islower(i):
			new_string += i
		else:
			new_string += chr(ord(i) + 32)
	return new_string

def my_upper(string):
	'''
	   Return a new string  converted to uppercase.
		string: given string
	'''
	new_string = ''
	for i in string:
		if string_isupper(i):
			new_string += i
		else: 
			new_string += chr(ord(i) - 32)
	return new_string

def my_split(string, element = ' '):
	tmp = ''
	total_list = []
	for i in string:
		if i == element:
			if tmp == '':
				continue
			else:
				total_list.append(tmp)
				tmp = ''
		else:
			tmp += i
	if tmp != '':
		total_list.append(tmp)
	return total_list

def my_strip(string):
    for i in string:
        if i != ' ':
            index1 = element_by_index(string, i) 
            break
    for i in range(len(string) - 1, index1, -1):
        if string[i] != ' ':
            index2 = i
            break
    return my_sss(string, index1, index2 + 1)


