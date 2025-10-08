from netmiko import ConnectHandler

raw_vrf_list = []
device = ['192.168.255.11','192.168.255.12','192.168.255.13']
for ip in device:

    cisco_881 = {
        'device_type': 'cisco_ios',
        'host':   ip,
        'username': 'rudy',
        'password': 'cisco',
        }
    net_connect = ConnectHandler(**cisco_881)
    output = net_connect.send_command('show ip vrf')
    print('Connecting to {}: '.format(ip))

    with open('output.txt', 'w') as f:
        f.write(output)
    with open('output.txt', 'r') as file:
        next(file)
        content = file.readlines()
        for i in content:
            word = i.split()
            vrf = word[0]
            raw_vrf_list.append(vrf)
vrf_list = list(set(raw_vrf_list))

with open('vrf_list.txt','w') as f:
    for item in vrf_list:
        f.write(item + '\n')

for ip in device:
    cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   ip,
    'username': 'rudy',
    'password': 'cisco',
    }
    
    net_connect = ConnectHandler(**cisco_881)
    for a in vrf_list:
        command = 'show ip route vrf ' + a
        print(command)
        output = net_connect.send_command(command)
        filename = a+ip
        print(filename)
        with open(filename, 'w') as z:
            z.write(output)
