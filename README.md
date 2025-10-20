The main function has x options
option 1 is for listing of all the interfaces on a device and displaying it's IP address
option 2 is for get the version information of multiple devcies that are entered as input
option 3 will configure the lo0 interface with first 3 octets as 172.16.255 and the last octet will be the last octet of the management interface IP address
 option 4 will login to every device in the list and find the available VRFs and output a file in the current directory will the unique list of the discovered VRFs
 option 5 will take a backup of all the VRF routing table discovered in option 4
 option 6 will require the user to input a VRF name and will create files with the entered VRF's routing table accross all devices, compare with the files created in option 5 and output the difference in the VRF route table
