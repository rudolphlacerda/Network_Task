from netmiko import ConnectHandler
import glob
import os

def compare_current(names):

	# Define the name of the customer who's current route table needs to be compared to the backup route table
	cust_vrf = input('Enter name of the customer VRF you want to compare with backup: ')

	device = ['192.168.255.11','192.168.255.12','192.168.255.13']

	# this loop will go over every device in the device list
	for ip in device:

		cisco_881 = {
			'device_type': 'cisco_ios',
			'host':   ip,
			'username': 'rudy',
			'password': 'cisco',
			}


	# This block will login to every router in the list to check for the inputted VRF
		net_connect = ConnectHandler(**cisco_881)
		output = net_connect.send_command('show ip vrf')
		read_output = output.split()
		if cust_vrf in output:
			print('Capturing the routing table of {} on {}'.format(cust_vrf,ip))
			route_table_command = 'show ip route vrf ' + cust_vrf
			route_table = net_connect.send_command(route_table_command)
			noutput = cust_vrf + ip + 'current' # Define the file name
			with open(noutput, 'w') as f:
				f.write(route_table)
		else:
			print('{} does not have this vrf, moving to the next device'.format(ip))
			continue
			
	textfile1_input = cust_vrf+'*'+'backup'
	textfile2_input = cust_vrf+'*'+'current'
	print(textfile1_input)
	text_files2 = glob.glob(textfile2_input)
	text_files1 = glob.glob(textfile1_input)
	print(text_files1)
	print(text_files2)

	for i in text_files1:
		for j in text_files2:
			if i[:-6] == j[:-7]:
				craft_command = 'diff {} {}'.format(i,j)
				os.system(craft_command)
		    



