from netmiko import ConnectHandler
def interface_display(names):

    for ip in names:

        cisco_881 = {
            'device_type': 'cisco_ios',
            'host':   ip,
            'username': 'rudy',
            'password': 'cisco',
            }
        net_connect = ConnectHandler(**cisco_881)
        output = net_connect.send_command('show ip int brief')
        print('Connecting to {}: '.format(ip))
        print(output)


