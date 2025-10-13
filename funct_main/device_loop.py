from netmiko import ConnectHandler
def conf_lo(names):

    for ip in names:

        cisco_881 = {
            'device_type': 'cisco_ios',
            'host':   ip,
            'username': 'rudy',
            'password': 'cisco',
            }
        net_connect = ConnectHandler(**cisco_881)

        last_octet = ip[-2::]
        lo_ip = '172.16.0.' + last_octet + ' 255.255.255.255'

        config_commands = [ 'int lo0',
                            'ip address lo_ip',
                          ]
        output = net_connect.send_config_set(config_commands)
        print('Connecting to {}: '.format(ip))
        print('IP address configured on Loopback 0 is {}: '.format(lo_ip))
