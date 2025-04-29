'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use command: python reg2.py SOFTWARE
'''

import sys
from regipy.registry import RegistryHive

try:
    #Gets the path to the registry hive from command like args
    hive_path = sys.argv[1]
    #Loads registry hive using registry class
    reg = RegistryHive(hive_path)

    print(f"Analyzing {hive_path}...")

    #Attempts to retrieve current version key under Software
    software_key = reg.get_key(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    if software_key:
        #If the key exists will extract and print the values
        print("\tProduct name:", software_key.get_value("ProductName"))
        print("\tCurrentVersion:", software_key.get_value("CurrentVersion"))
        print("\tServicePack:", software_key.get_value("CSDVersion"))
        print("\tProductID:", software_key.get_value("ProductId"))

    else:
        #Notifies user if it does not exist
        print("Subkey 'CurrentVersion' not found in the provided registry file.")

#Handles if the hive does not exist
except FileNotFoundError as exception:
    print(f"Registry hive file not found: {exception}")

#Catches and displays all other errors
except Exception as exception:
    print(f"An error occurred: {exception}")
