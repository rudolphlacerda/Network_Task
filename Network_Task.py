from netmiko import ConnectHandler
import socket
import glob
import os
from pathlib import Path

class DeviceClass():
    def __init__(self,passedlist):
        self.passedlist = passedlist
        print('''What do you want to do? \n 
              1. See the interfaces of the devices and their IP \n 
              2. See the version of the devices \n
              3. Confgure Loopback IP for each devce \n
              4. Get a list of vrf on all devices \n
              5. Take a backup of all discovered vrf on all devices\n
              6. Compare a VRF's current table with it's backup''')
        

    def interface_display(self):

        for ip in self.passedlist:

            cisco_881 = {
                'device_type': 'cisco_ios',
                'host':   ip,
                'username': 'rudy',
                'password': 'cisco',
	        }
            net_connect = ConnectHandler(**cisco_881)
            output = net_connect.send_command('show ip int brief')
            print('Connecting to {}: '.format(ip))
            print(output + '\n\n')
            
    def show_version(self):
        for ip in self.passedlist:
            cisco_881 = {
                'device_type': 'cisco_ios',
                'host':   ip,
                'username': 'rudy',
                'password': 'cisco',
                }
            net_connect = ConnectHandler(**cisco_881)
            output = net_connect.send_command('show version')
            print('Connecting to {}: '.format(ip))

            with open('output.txt', 'w') as f:
                f.write(output)
            with open('output.txt', 'r') as file:
                content = file.read()
            word = content.split()

            index1 = word.index('Version')
            index2 = index1 + 2
            print(word[index1:index2])
            print('\n')
            
    def conf_lo(self):

        for ip in self.passedlist:

            cisco_881 = {
                'device_type': 'cisco_ios',
                'host':   ip,
                'username': 'rudy',
                'password': 'cisco',
                }
            net_connect = ConnectHandler(**cisco_881)
            convert_to_ip = socket.gethostbyname(ip)
            print(convert_to_ip)
            last_octet =  convert_to_ip[-2::]
            lo_ip = 'ip address ' + '172.16.0.' + last_octet + ' 255.255.255.255'

            config_commands = [ 'int lo0',
                                lo_ip,
                              ]
            print(config_commands)
            output = net_connect.send_config_set(config_commands)
            print('Connecting to {}: '.format(ip))
            print('IP address configured on Loopback 0 is {}: '.format(lo_ip))

    def get_vrf_list(self):

        raw_vrf_list = []

        for ip in self.passedlist:

            cisco_881 = {
                'device_type': 'cisco_ios',
                'host':   ip,
                'username': 'rudy',
                'password': 'cisco',
                }
            net_connect = ConnectHandler(**cisco_881)
            output = net_connect.send_command('show ip vrf')
            print('Connecting to {}: '.format(ip))
            output_file = Path("./OutPutDir/output.txt")
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w') as f:
                f.write(output)
            with open(output_file, 'r') as file:
                next(file)
                content = file.readlines()
                for i in content:
                    word = i.split()
                    if len(word) < 2:
                        pass
                    else:
                        vrf = word[0]
                        raw_vrf_list.append(vrf)
        vrf_list = list(set(raw_vrf_list))

        with open('vrf_list.txt','w') as f:
            for item in vrf_list:
                f.write(item + '\n')       
                
    def    vrf_tables_backup(self):
        with open('vrf_list.txt','r') as f:
            vrf_list = f.read().split()


        for v in vrf_list:
            for ip in self.passedlist:

                cisco_881 = {
                    'device_type': 'cisco_ios',
                    'host':   ip,
                    'username': 'rudy',
                    'password': 'cisco',
                    }
                
                net_connect = ConnectHandler(**cisco_881)
                route_table_command = 'show ip route vrf ' + v
                route_table = net_connect.send_command(route_table_command)
                output = net_connect.send_command('show ip vrf')
                if v in output:
                    print('vrf {} in router {}'.format(v,ip))
                    filename = v+ip+'backup'
                    #print(filename)
                    with open(filename, 'w') as z:
                        z.write(route_table)
                else:
                    continue
                    


    def compare_current(self):

        # Define the name of the customer who's current route table needs to be compared to the backup route table
        cust_vrf = input('Enter name of the customer VRF you want to compare with backup: ')


        # this loop will go over every device in the device list 
        for ip in self.passedlist:

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
        #print(textfile1_input)
        text_files2 = glob.glob(textfile2_input)
        text_files1 = glob.glob(textfile1_input)
        print(text_files1)
        print(text_files2)

        for i in text_files1:
            for j in text_files2:
                if i[:-6] == j[:-7]:
                    craft_command = 'diff {} {}'.format(i,j)
                    os.system(craft_command)     
							
