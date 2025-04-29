'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use command: python reg1.py SOFTWARE
Remember to run in windows command prompt
'''

import sys
import winreg

try:
    #Connect to the HKEY_LOCAL_MACHINE root of the windows registry
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

    #Get registry path from command line
    key_path = sys.argv[1]

    #Open specified Key path
    key = winreg.OpenKey(reg, key_path)

    print(f"Analyzing {key_path} in Windows registry...")

    #Gets the last modified timestamp
    last_modified = winreg.QueryInfoKey(key)[2]
    print(f"Last modified: {last_modified} [UTC]")

    try:
        #Loops through all subkeys under main registry
        for i in range(winreg.QueryInfoKey(key)[1]):

            #Gets the subkey name
            subkey_name = winreg.EnumKey(key, i)
            print("Subkey:", subkey_name)

            #Opens subkey for reading
            subkey = winreg.OpenKey(key, subkey_name)
            try:
                j = 0
                while True:
                    try:
                        #Enumerates all values within the subkey
                        value_name, value_data, _ = winreg.EnumValue(subkey, j)
                        print(f"Name: {value_name}, Value path: {value_data}")
                        j += 1
                    except OSError as e:
                        #Indicates error if no more data
                        if e.errno == 259:
                            break
                        else:
                            raise
            except OSError:
                pass
            print("\n")

    except OSError as e:
        if e.errno == 259:
            pass
        else:
            raise

#Handles the case of if the registry key does not work
except FileNotFoundError as e:
    print("Registry key not found:", e)

#Handles the lack of permission to access key
except PermissionError as e:
    print("Permission error:", e)

#Handles any other unexpected errors
except Exception as e:
    print("An error occurred:", e)
