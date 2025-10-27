from funct_main import count_of_devices
from funct_main import input_device_list
from funct_main import interface_brief
from funct_main import device_version
from funct_main import device_loop
from funct_main import get_list_of_vrf
from funct_main import backup_vrf_tables
from funct_main import current_vrf_tables

num = count_of_devices.num_of_device() # The selected option in the menu will run on the number of devices specified


print('''What do you want to do? \n 
     1. See the interfaces of the devices and their IP \n 
     2. See the version of the devices \n
     3. Confgure Loopback IP for each devce \n
     4. Get a list of vrf on all devices \n
     5. Take a backup of all discovered vrf on all devices\n
     6. Compare a VRF's current table with it's backup''')

menu_choice = count_of_devices.menu_options()


if menu_choice == 1:
    names = input_device_list.name_of_device(num)
    interface_brief.interface_display(names)

elif menu_choice == 2:

    names = input_device_list.name_of_device(num)
    device_version.show_version(names)

elif menu_choice == 3:

    names = input_device_list.name_of_device(num)
    device_loop.conf_lo(names)

elif menu_choice == 4:

    names = input_device_list.name_of_device(num)
    get_list_of_vrf.get_vrf_list(names)
    
elif menu_choice == 5:

    names = input_device_list.name_of_device(num)
    backup_vrf_tables.vrf_tables_backup(names)
    
elif menu_choice == 6:
    names = input_device_list.name_of_device(num)
    current_vrf_tables.compare_current(names)
