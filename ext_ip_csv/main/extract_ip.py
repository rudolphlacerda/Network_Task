import csv

def ip_from_csv():
    list_of_ip = []
    with open('samplecsvfile.csv',mode='r',newline='') as f: #if csv has special chars like '@' for email address use encoding ='UTF-8'
        reader = csv.reader(f)
        for row in reader:
            list_of_ip.append(row[2])
        
    return list_of_ip[1:]
