'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - dca-hw.py
NOTE: Use files: dca-log.csv & dca-db.db .
'''

import csv
import sqlite3

#Reads log data from the csv file and returns it as a list of dictionaries
def retrieve_log_data(log_file):
    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

#Connects to the SQLite database, fethces the info and returns them
def retrieve_database_data(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    #Executes query to retrieve the data from all the users
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    #Closes connection
    conn.close()

    #Converts each row into dictionary
    return [{'id': row[0], 'username': row[1], 'role': row[2], 'email': row[3], 'website': row[4]} for row in rows]

#Displays list of usernames form the log and prompts user to choose
def prompt_for_username(log_data):
    print("Available usernames:")
    for i, entry in enumerate(log_data):
        print(f"{i + 1}. {entry.get('username')}")

    selection = int(input("Select a username by entering its number: ")) - 1
    return log_data[selection].get('username').strip()

#Finds all the log entries that correlate with the username and prints them
def correlate_data_based_on_user_input(database, log_data, selected_username):

    #Filters the log data for entries that match
    correlated_data = [entry for entry in log_data if entry.get('username').strip() == selected_username]

    if correlated_data:
        print(f"\nCorrelated data for '{selected_username}':")
        for entry in correlated_data:
            print(entry)
    else:
        print(f"No data found for the entered username '{selected_username}'.")

#Prompts user for CSV log file
log_file = input("Enter the log file name (e.g., logfile.csv): ")

#Prompts user for SQLite database file
db_file = input("Enter the database file name (e.g., local_db_file.db): ")

#Loads log and database data
log_data = retrieve_log_data(log_file)
database = retrieve_database_data(db_file)

#Prompts user to select a username from the log
selected_username = prompt_for_username(log_data)

#Performs the correlation and matches the results
correlate_data_based_on_user_input(database, log_data, selected_username)
