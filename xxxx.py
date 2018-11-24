number = int(input('please enter any integer number:'))
temp = number

while number > 0:
	count = temp
	while count >0:
		print('*', end='')
		count = count - 1
	print()
	number = number -1
