from netmiko import ConnectHandler
with open('vrf_list.txt','r') as f:
    vrf_list = f.read().split()
    #print(vrf_list)
device = ['192.168.255.11','192.168.255.12','192.168.255.13']
for v in vrf_list:
    for ip in device:

        cisco_881 = {
            'device_type': 'cisco_ios',
            'host':   ip,
            'username': 'rudy',
            'password': 'cisco',
            }
        #print('Connecting to {}: '.format(ip))
        net_connect = ConnectHandler(**cisco_881)
        route_table_command = 'show ip route vrf ' + v
        route_table = net_connect.send_command(route_table_command)
        output = net_connect.send_command('show ip vrf')
        if v in output:
            print('vrf {} in router {}'.format(v,ip))
            filename = v+ip+'current'
            print(filename)
            with open(filename, 'w') as z:
                z.write(route_table)
