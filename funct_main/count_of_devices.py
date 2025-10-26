def num_of_device():
	c = 0
	while c<1:
		try:
    			num = int(input('Please enter the number of devices: '))
    			c += 1
		except:
			print('Please enter a numberic value')
	return num
