# ISS 212 CS Scripting - WK 8 TD 6- Python Suspicious IP Address Extraction
# Bash script using Regex -- Redacting data using pattern matching
#Add Lauren Mathews and 3/24/25 to the first comment line.
#ISS 212 - CS Scripting - Python Script: ipextract
#Citations: Jen Moody

import re

# Opens the auth.log and reads the file
with open('auth.log', 'r') as file:
	log_data = file.read()

# Searching for a pattern of failed password attempts
pattern = r"Failed password .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# Looks for a pattern of failed passwords and the associated IPs in the log data
suspicious_ips = re.findall(pattern, log_data)

# Prints any suspicious IP addresses
unique_ips = set(suspicious_ips)
print("Suspicious IP addresses:")
for ip in unique_ips:
	print(ip)
