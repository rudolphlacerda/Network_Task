import glob
import difflib
import os

cust_vrf = input('Enter customer vrf name: ')
textfile1_input = cust_vrf+'*'+'backup'
textfile2_input = cust_vrf+'*'+'current'
print(textfile1_input)
text_files2 = glob.glob(textfile2_input)
text_files1 = glob.glob(textfile1_input)
print(text_files1)
print(text_files2)

for i in text_files1:
    for j in text_files2:
        if i[:-6] == j[:-7]:
            craft_command = 'diff {} {}'.format(i,j)
            os.system(craft_command)
            


        
