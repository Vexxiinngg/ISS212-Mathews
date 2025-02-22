#Bash Block 1. Network Traffic Analysis
#Resources Bash Scenario 1 Example Script
#Prompt the user to input the packet size in bytes and store them as an integer

read -p "Enter the packet size in bytes: " packet_size
 if [ "$packet_size" -ge 100 ]; then

#True if the packet size is bigger than or equal to 100
 	echo "True - Packet meets the threshold for analysis."
 else
#Say False otherwise
 	echo "False - Packet is too small to analyze."
 fi

# Bash Block 2. Protocol Identification
#Resources: Bash Scenario 2 Example Script

#Prompt user to input protocol name and store in the variable
read -p "Enter the protocol name: " protocol_name
#Check if the protocol name is exactly "Cyphersec"
 if [ "$protocol_name" == "Cyphersec" ]; then
#Prints message saying that Cyphersec is the best protocol ever
 	echo "Yes - Cyphersec is the best protocol ever!"
#Check if the protocol name is cyphersec
 elif [ "$protocol_name" == "cyphersec" ]; then
 #Prints deny message for the cybersec saying no I want big Cyphersec
 	echo "No, I want a big Cyphersec!"
 else
 #If the input is neither print a message with the entered protocol name
 	echo "Cyphersec! Not $protocol_name!"
 fi

#Bash Block 3. Data Security Tax Calculation
# Resources: Bash Scenario 3: Data Security Tax Calculation Example Script
read -p "Enter your annual data usage in MB: " data_usage
 if [ "$data_usage" -le 85528 ]; then
 	tax=$((data_usage * 18 / 100 - 556))
 else
 	surplus=$((data_usage - 85528))
 	tax=$((14839 + surplus * 32 / 100))
 fi
 if [ "$tax" -lt 0 ]; then
 	tax=0
 fi
 echo "Your Data Security Tax is: $tax MB"

# Block 4. Patch Cycle Determination
# Resources:Bash Scenario 4: Patch Cycle Determination Example Script

# Prompt the user to enter the year they want to check the patch cycle for
read -p "Enter the year to check the patch cycle: " year
 if [ "$year" -lt 2000 ]; then
 	echo "Not within the managed patch period."
 else
 	if (( year % 4 != 0 )); then
     	echo "Standard Year"
 	elif (( year % 100 != 0 )); then
     	echo "Patch Year"
 	elif (( year % 400 != 0 )); then
     	echo "Standard Year"
 	else
     	echo "Patch Year"
 	fi
 fi