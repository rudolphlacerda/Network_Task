def num_of_device():
	c = 0
	while c<1:
		try:
    			num = int(input('Please enter the number of devices: '))
    			c += 1
		except:
			print('Please enter a numberic value')
	return num

def menu_options():

	while True:
		try:
			selection = int(input('Please enter a number from the menu: '))
			if selection < 7:
				break

		except:
			print('Please enter a number between 1-6')
	return selection
