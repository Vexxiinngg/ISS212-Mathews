'''

ISS 212 - Mini Tool Builder – Scan Host & Ports
3.2025 Wk 10 Assignment 6
Citation: Jen Moody
Purpose:
'''

import socket
import datetime

# Prompt user for domain and handle invalid input
host = input("Enter domain: ")

try:
    #Attemp to resolve domain to IP address
    ip = socket.gethostbyname(host)
    print(f"\nScanning {ip} (resolved from {host})...\n")

    open_ports = [] #A List to store any ports that have been found
    #Scan ports 20 - 26
    for port in range(20, 26):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        sock.close()

    # A Summary with  the timestamp of the outputs
    #Prints scan completion Time
    print("\nScan complete at", datetime.datetime.now())
    #Displays a summary of the ports
    if open_ports:
        print("Open ports:", ', '.join(str(p) for p in open_ports))
    else:
        print("No open ports found in the range 20–25.")
#Handles the case if the domain is invalid or cant be resolved
except socket.gaierror:
    print("Error: Invalid domain name. Please try again.")