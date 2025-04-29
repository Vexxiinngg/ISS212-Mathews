'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use Command: python reg3.py SYSTEM
'''

import winreg
import sys

#Retrieves current active control set from the system key
def getCurrentControlSet():
    try:
        hkey_local_machine = winreg.HKEY_LOCAL_MACHINE
        select_subkey = "SYSTEM\\Select"

        #Opens the selct key and stores the control set
        with winreg.OpenKey(hkey_local_machine, select_subkey) as key:
            #Loops through each values to find current one
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                value_name, value_data, _ = winreg.EnumValue(key, i)
                if value_name == "Current":
                    # Returns index of current control set
                    return value_data
    except FileNotFoundError as exception:
        print("Couldn't find SYSTEM\\Select key ", exception)

#Maps the service type to readable descriptions and prints that service info
def getServiceInfo(dictionary):
    serviceType = {
        1: "Kernel device driver", 2: "File system driver", 4: "Arguments for an adapter",
        8: "File system driver interpreter", 16: "Own process", 32: "Share process",
        272: "Independent interactive program", 288: "Shared interactive program"
    }
    #Prints the basic service details
    print(" Service name: %s" % dictionary["SERVICE_NAME"])
    if "DisplayName" in dictionary:
        print(" Display name: %s" % dictionary["DisplayName"])

    if "ImagePath" in dictionary:
        print(" ImagePath: %s" % dictionary["ImagePath"])

    if "Type" in dictionary:
        print(" Type: %s" % serviceType.get(dictionary["Type"], "Unknown"))

    if "Group" in dictionary:
        print(" Group: %s" % dictionary["Group"])

    print("--------------------------")

#Collects all the perams from a specific subkey and then it send them to be printed
def serviceParams(subkey):
    service = {}
    #Stores subkey name
    service["SERVICE_NAME"] = subkey
    service["ModifiedTime"] = winreg.QueryInfoKey(subkey)[2]

    try:
        #Reads all values from the subkey and stores them in service dict.
        for i in range(0, winreg.QueryInfoKey(subkey)[1]):
            value_name, value_data, _ = winreg.EnumValue(subkey, i)
            service[value_name] = value_data
    except OSError as exception:
        print("Error accessing registry subkey ", exception)

    #Prints out the service info
    getServiceInfo(service)

#enumerates and processes all services in active control set
def servicesKey(controlset):
    serviceskey = "SYSTEM\\ControlSet00%d\\Services" % controlset
    try:
        #Opens the service key of current set
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, serviceskey) as key:
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                #Each service listed as a subkey
                subkey_name = winreg.EnumKey(key, i)
                #Opens individual subkeys
                subkey = winreg.OpenKey(key, subkey_name)
                #Analyzes and prints the service details
                serviceParams(subkey)
    except FileNotFoundError as exception:
        print("Couldn't find Services key ", exception)

if __name__ == "__main__":
    controlset = getCurrentControlSet()
    if controlset is not None:
        servicesKey(controlset)
