#
#
# Resources: Python Scenario 3: Data Security Tax Calculation Example Script

# Prompt the user to input  annual data usage in MB and store it as a floating-point number
data_usage = float(input("Enter your annual data usage in MB: "))
# Check to see if the data usage is less than or equal to 85,528 MB
if data_usage <= 85528:
    # If the data usage is below or equal to 85,528 MB, apply the tax calculation formula for below or equal usage
	tax = (0.18 * data_usage) - 556.02
else:
    # If the data usage is above 85,528 MB, apply the tax calculation formula for greater usage
	tax = 14839.02 + 0.32 * (data_usage - 85528)
	# Ensure the tax is not negative, then set to 0
tax = max(tax, 0)
# Print the calculated data security tax
print(f"Your Data Security Tax is: {round(tax)} MB")
