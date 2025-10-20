from netmiko import ConnectHandler
import socket

def conf_lo(names):

    for ip in names:

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
        #print('Connecting to {}: '.format(ip))
        #print('IP address configured on Loopback 0 is {}: '.format(lo_ip))
