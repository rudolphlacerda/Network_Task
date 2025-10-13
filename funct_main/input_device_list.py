def name_of_device(num):
    index = 0
    devices = []
    while index < num:
        for d in range(num):
            str = input('name/IP of device: ')
            index += 1
            devices.append(str)

    return devices
