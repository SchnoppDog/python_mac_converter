import requests
import time

class macAddressConverter:
    """
    A class to format a mac-address to other often used formats

    Attributes
    ----------
    macAddress => str
        representing the mac-address provided by setMacAddress
    macAddressList => list
        a list containing multiple mac-addresses to format
    
    Methods
    -------
    printSupportFormats()
        prints all supported mac-addresses for formatting
    setMacAddress(macAdress=list)
        setting the mac-address
    getMacFormat1()
        returns the mac-address i.e. 00-80-41-ae-fd-7e
    getMacFormat2()
        returns the mac-address i.e. 008041-aefd7e
    getMacFormat3()
        returns the mac-address i.e. 00:80:41:ae:fd:7e
    getMacFormat4()
        returns the mac-address i.e. 008041aefd7e
    getMacFormat5()
        returns the mac-address i.e. 0080.41ae.fd7e
    getMacFormatAll()
        returns the mac-address in all formats
    getMacVendor(macAddressList=list)
        returns the vendor of the mac-address
    """

    def __init__(self) -> None:
        """
        Initiates the converter

        Parameters
        ----------
        No parameters needed

        Returns
        -------
        Passing return
        """

        self.macAddress         = None
        self.__macPlainString   = None
        pass

    def printSupportFormats(self) -> print:
        """
        Prints all supported mac-address formatsk

        Parameters
        ----------
        No parameters needed

        Returns
        -------
        Nothing
        """
        print('Supported mac-address formats are: ')
        print('1. 00-80-41-ae-fd-7e')
        print('2. 008041-aefd7e')
        print('3. 00:80:41:ae:fd:7e')
        print('4. 008041aefd7e')
        print('5. 0080.41ae.fd7e')

    def setMacAddress(self, macAddress: list) -> list:
        """
        Sets the mac-address for the instance. Can be multiple mac-addresses.
        
        Parameters
        ----------
        macAddress => list\n\r
            A list containg one or multiple mac-addresses as string
        
        Returns
        -------
        Nothing
        """
        macAddressList = []

        for mac in macAddress:
            m = mac.strip().replace('-', '').replace(':', '').replace('.', '')
            macAddressList.append(m)
        self.__macPlainString = macAddressList

    def getMacFormat1(self) -> list:
        """
        Returns the mac-address(es) in the format of 00-80-41-ae-fd-7e
        
        Parameters
        ----------
        No parameters needed

        Returns
        -------
        macAddressList => list\n\r
            Returns a list containing the mac-address(es) in the format of 00-80-41-ae-fd-7e
        """

        macAddressList = []

        for macAddress in self.__macPlainString:
            macAddress = macAddress[:2] + '-' + macAddress[2:4] + '-' + macAddress[4:6] + '-' + macAddress[6:8] + '-' + macAddress[8:10] + '-' + macAddress[10:12]
            macAddressList.append(macAddress)

        return macAddressList

    def getMacFormat2(self) -> list:
        """
        Returns the mac-address(es) in the format of 008041-aefd7e

        Parameters
        ----------
        No parameters needed

        Returns
        -------
        macAddressList => list\n\r
            Returns a list containing the mac-address(es) in the format of 008041-aefd7e
        """

        macAddressList = []
        for macAddress in self.__macPlainString:
            macAddress = macAddress[:6] + '-' + macAddress[6:12]
            macAddressList.append(macAddress)

        return macAddressList

    def getMacFormat3(self) -> list:
        """
        Returns the mac-address(es) in the format of 00:80:41:ae:fd:7e

        Parameters
        ----------
        No parameters needed

        Returns
        -------
        macAddressList => list\n\r
            Returns a list containing the mac-address(es) in the format of 00:80:41:ae:fd:7e
        """

        macAddressList = []

        for macAddress in self.__macPlainString:
            macAddress = macAddress[:2] + ':' + macAddress[2:4] + ':' + macAddress[4:6] + ':' + macAddress[6:8] + ':' + macAddress[8:10] + ':' + macAddress[10:12]
            macAddressList.append(macAddress)
        
        return macAddressList

    def getMacFormat4(self) -> list:
        """
        Returns the mac-address(es) in the format of 008041aefd7e

        Paramters
        ---------
        No parameters needed

        Returns
        -------
        macAddressList => list\n\r
            Returns a list containing the mac-address(es) in the format of 008041aefd7e
        """

        macAddressList = self.__macPlainString
        return macAddressList

    def getMacFormat5(self) -> list:
        """
        Returns the mac-address(es) in the format of 0080.41ae.fd7e

        Parameters
        ----------
        No parameters needed

        Returns
        -------
        macAddressList => list\n\r
            Returns a list containing the mac-address(es) in the format of 0080.41ae.fd7e
        """

        macAddressList = []

        for macAddress in self.__macPlainString:
            macAddress = macAddress[:4] + '.' + macAddress[4:8] + '.' + macAddress[8:12]
            macAddressList.append(macAddress)
        
        return macAddressList

    def getMacFormatAll(self) -> list:
        """
        Returns the mac-address(es) in all formats

        Parameters
        ----------
        No parameters needed

        Returns
        -------
        macAddressFormatList => list\n\r
            Returns a list containing all the mac-address formats
        """

        macAddressFormatList = []
        macAddressFormatList.append(self.getMacFormat1())
        macAddressFormatList.append(self.getMacFormat2())
        macAddressFormatList.append(self.getMacFormat3())
        macAddressFormatList.append(self.getMacFormat4())
        macAddressFormatList.append(self.getMacFormat5())

        return macAddressFormatList

    def getMacVendor(self, macAddressList: list) -> list:
        """
        Returns the vendor of the mac-address(es)

        Parameters
        ----------
        macAddressList => list\n\r
            A list containing the mac-address(es)

        Returns
        -------
        macVendorDict => dict\n\r
            A dict containing the vendor the mac-address(es)
        """

        macVendorDict   = {}
        counter         = 0

        for mac in macAddressList:
            response                    = requests.get(f'https://api.macvendors.com/{mac}')
            macVendor                   = response.text.strip()
            macVendorDict[counter]      = {}
            macVendorDict[counter][mac] = macVendor
            counter += 1
            time.sleep(1)
        
        return macVendorDict