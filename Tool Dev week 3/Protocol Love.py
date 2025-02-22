#ISS 212 CS Scripting - WK 3 - Assignment 3
#Resources: Python Scenario 2 Example Script

#Prompt user to input protocol name and store in the variable
protocol_name = input("Enter the protocol name: ")
#Check if the protocol name is exactly "Cyphersec"
if protocol_name == "Cyphersec":
    #Prints message saying that Cyphersec is the only supported protocol
	print("Cyphersec is the only supported protocol!")
	#Check if the protocol name is cybersec
elif protocol_name == "cybersec":
    #Prints deny message for the cybersec protocol
	print("DENIED. Cyphersec protocol ONLY!")
else:
    #If the input is neither print a message with the entered protocol name
	print(f"Cyphersec! Not {protocol_name}!")