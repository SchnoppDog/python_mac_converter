from c_mac_address_converter import macAddressConverter

macConverter    = macAddressConverter()
macAddressList  = []
oldMacList      = []
macFormat       = None
multipleIps     = None
getVendor       = None
macVendor       = None
macAddress      = None
oldMacAddress   = None
objLen          = None
counter         = None
counterList     = None

macConverter.printSupportFormats()

macFormat   = input('\nChoose your format: ')
multipleIps = input('Do you want to convert multiple MAC addresses (y/n): ')
getVendor   = input('Do you want to get the vendor for your MAC address (y/n): ')

if multipleIps.lower() == 'n':
    macAddress = input('\nType your MAC address: ')
    macConverter.setMacAddress([macAddress])

    oldMacAddress = macAddress

    if macFormat == '1':
        macAddress = macConverter.getMacFormat1()
    elif macFormat == '2':
        macAddress = macConverter.getMacFormat2()
    elif macFormat == '3':
        macAddress = macConverter.getMacFormat3()
    elif macFormat == '4':
        macAddress = macConverter.getMacFormat4()
    elif macFormat == '5':
        macAddress = macConverter.getMacFormat5()
    else:
        macAddress = macConverter.getMacFormatAll()
    
    for mac in macAddress:
        print('\n############# Converted MAC #############')
        print(f'{oldMacAddress} ==> {mac}')

    if getVendor.lower() == 'y':
        print('\n############# Vendor #############')
        macVendor   = macConverter.getMacVendor(macAddress)
        objLen      = len(macVendor)

        for obj in range(0, objLen):
            for key, value in macVendor[obj].items():
                print(f'{key} ==> {value}')


elif multipleIps.lower() == 'y':
    counter = int(input('How many addresses do you want to convert: '))
    print('\n')

    for _ in range(0, counter, 1):
        macAddress = input('Type your MAC address: ')
        macAddressList.append(macAddress)
        
    print('\n')
    oldMacList = macAddressList
    
    macConverter.setMacAddress(macAddressList)

    if macFormat == '1':
        macAddressList = macConverter.getMacFormat1()
    elif macFormat == '2':
        macAddressList = macConverter.getMacFormat2()
    elif macFormat == '3':
        macAddressList = macConverter.getMacFormat3()
    elif macFormat == '4':
        macAddressList = macConverter.getMacFormat4()
    elif macFormat == '5':
        macAddressList = macConverter.getMacFormat5()
    else:
        macAddressList = macConverter.getMacFormatAll()

    print('\n############# Converted MAC #############')
    counterList = 0
    for mac in macAddressList:
        print(f'{oldMacList[counterList]} ==> {mac}')
        counterList += 1

    if getVendor.lower() == 'y':
        print('\n############# Vendor #############')
        macVendor   = macConverter.getMacVendor(macAddressList)
        objLen      = len(macVendor)

        for obj in range(0, objLen):
            for key, value in macVendor[obj].items():
                print(f'{key} ==> {value}')

else:
    print('Quitting Script')