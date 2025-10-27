import schedule
import time
from datetime import datetime
from netmiko import ConnectHandler
import device_list
import glob
import os
import smtplib
import getpass

def currentrun_compare():
# Setting up Gmail account to send mails on mismatch
	smtp_object = smtplib.SMTP('smtp.gmail.com',587)
	smtp_object.ehlo()
	smtp_object.starttls()

# Iterate through the list of devices that should be in the same location as this script file 	
	for ip in device_list.sample_data:
		cisco_881 = {
		'device_type': 'cisco_ios',
		'host':   ip,
		'username': 'rudy',
		'password': 'cisco',
		}
		
		net_connect = ConnectHandler(**cisco_881)
		show_run = net_connect.send_command('show run')

# This block will do a show run on each device and creat a file with name "deviceIPcurrent"		
		filename = ip + 'runcurrent'
		with open(filename , 'w') as f:
			f.write(show_run)

# This block will compare the DeviceIPcurrent with the DeviceIPmaster taken with the script "master_backup"			
		textfile1 = ip + 'runmaster'
		textfile2 = ip + 'runcurrent'
		command_structure = 'diff ' + textfile1 + " " + textfile2
		difference = os.system(command_structure)
		str_difference = str(difference)
		if difference == 0:
			print("There is no difference on {}".format(ip))


		else:
			print('This is the difference {} on {}: '.format(difference,ip))
			email = getpass.getpass('email: ')
			password = getpass.getpass('Password: ')
			smtp_object.login(email,password)
			from_address = email
			to_address = email
			subject = 'Difference on ' + ip
			message = str_difference
			print(str_difference)
			msg = "Subject: "+subject+'\n'+message
			
			smtp_object.sendmail(from_address,to_address,msg)
				
	print(f"Job executed at: {datetime.now()}")
	
		
schedule.every().day.at("10:30").do(currentrun_compare)

while True:
    schedule.run_pending()
    time.sleep(3600)
