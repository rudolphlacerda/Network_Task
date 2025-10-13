from netmiko import ConnectHandler
def show_version(names):

    for ip in names:

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
