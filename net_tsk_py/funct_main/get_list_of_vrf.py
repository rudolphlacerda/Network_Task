from netmiko import ConnectHandler

def get_vrf_list(names):

    raw_vrf_list = []

    for ip in names:

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
                if len(word) < 2:
                    pass
                else:
                    vrf = word[0]
                    raw_vrf_list.append(vrf)
    vrf_list = list(set(raw_vrf_list))

    with open('vrf_list.txt','w') as f:
        for item in vrf_list:
            f.write(item + '\n')
