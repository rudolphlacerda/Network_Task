from Network_Task import DeviceClass

list_of_ip = ['192.168.255.11','192.168.255.12','192.168.255.13']

mainclass = DeviceClass(list_of_ip)

action = int(input('Please enter your selection :'))
if action == 1:
    mainclass.interface_display()
    
if action == 2:
    mainclass.show_version()
    
if action == 3:
    mainclass.conf_lo()
    
if action == 4:
    mainclass.get_vrf_list()
    
if action == 5:
    mainclass.vrf_tables_backup()

if action == 6:
    mainclass.compare_current()
