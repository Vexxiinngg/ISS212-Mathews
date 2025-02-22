# ISS 212 CS Scripting - WK 3 - Assignment 3 sample script
#
# Resources:Python Scenario 4: Patch Cycle Determination Example Script

# Prompt the user to enter the year they want to check the patch cycle for
year = int(input("Enter the year to check the patch cycle: "))

# Check if the entered year is before the year 2019
if year < 2019:
    # If the year is before 2019, print a message that says it's not within the managed patch period
    print("Not within the managed patch period.")
else:
    # If the year is 2019 or later, check if the year is a leap year
    if year % 4 != 0:
        # If the year is not divisible by 4, print it is a standard year
        print("Standard Year")
    elif year % 100 != 0:
        # If the year is divisible by 4 but not by 100, print it's a patch year (leap year)
        print("Patch Year")
    elif year % 400 != 0:
        # If the year is divisible by 100 but not by 400, print it's a standard year
        print("Standard Year")
    else:
        # If the year is divisible by 400, print it's a patch year (leap year)
        print("Patch Year")
