# SP25 - ISS 212 Week 4 Tool Dev 2
# Works Cited - Jenn Moody
# Tool Dev Scenario 1
# Prompt the user to enter their role
role = input("Enter your role (admin, user, guest): ").strip().lower()

# Determine access level based on role
if role == "admin":
	print("Access Level: Full privileges granted.")
elif role == "user":
	print("Access Level: Limited privileges granted.")
elif role == "guest":
	print("Access Level: Read-only access granted.")
else:
	print("Invalid role entered. Please choose from admin, user, or guest.")
