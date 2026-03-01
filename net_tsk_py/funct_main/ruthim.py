class Ruthim():
	def __init__(self):
		pass

	
	def num_of_device(self):
		c = 0
		while c<1:
			try:
	    			num = int(input('Please enter the number of devices: '))
	    			c += 1
			except:
				print('Please enter a numberic value')
		return num

	def name_of_device(self,num):
		index = 0
		devices = []
		while index < num:
			for d in range(num):
			    str = input('name/IP of device: ')
			    index += 1
			    devices.append(str)

		return devices
		
		

