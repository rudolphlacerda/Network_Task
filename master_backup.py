#import schedule
import time
from datetime import datetime
from netmiko import ConnectHandler
import device_list

def master_backup():
	for ip in device_list.sample_data: # The file device_list.py needs to be in the same location as this script
		cisco_881 = {
		'device_type': 'cisco_ios',
		'host':   ip,
		'username': 'rudy',
		'password': 'cisco',
		}
		
		net_connect = ConnectHandler(**cisco_881)
		show_run = net_connect.send_command('show run')
		
		filename = ip + 'run' + 'master'
		with open(filename , 'w') as f:
			f.write(show_run)
			
	print(f"Job executed at: {datetime.now()}")

		
#schedule.every(7).days.at("10:30").do(master_backup)

#while True:
#    schedule.run_pending()
#    time.sleep(3600) 
