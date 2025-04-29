'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - bowser.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

import os
import sqlite3
from datetime import datetime

#The function to analyze the chrome browser history and save the results as an ouput file
def analyze_chrome_history(history_path, output_file):
    #Checking to see if the provided path is a valid file
    if not os.path.isfile(history_path):
        print("Invalid file path. Please make sure the file exists.")
        return

    try:
        #Connects to the SQLite database at the history path
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor() #Creating a cursor to interact with the data

        #Executing a query to fetch all from the URLS
        cursor.execute("SELECT * FROM urls")
        rows = cursor.fetchall()

        print("[--- Browser History Analysis ---]\n")
        #Opens the output file for writing the analysis
        with open(output_file, 'w', encoding='utf-8') as file:
            #Lopping through each row of fetched data
            for row in rows:
                url = row[1]
                last_visit_time_microseconds = row[5]

                #Checks to see of the visit time exists and is valid
                if last_visit_time_microseconds and last_visit_time_microseconds < 2**63:
                    try:

                        #Converts the lasty time visited into microseconds
                        visit_time = datetime.fromtimestamp(
                            (last_visit_time_microseconds - 11644473600000000) / 1000000
                        ).strftime('%Y-%m-%d %H:%M:%S')
                    except (ValueError, TypeError) as e:
                        #If an error in conversation appears will print an error message
                        print(f"Error converting visit time: {e}")
                        visit_time = "N/A"
                else:
                    #If the visit time is not valid will set it to NA
                    visit_time = "N/A"

                #Formats the output line with the URL and the visit time
                output_line = f"[+] URL: {url}\n   Last Visit Time: {visit_time}\n"
                print(output_line)
                file.write(output_line)

        #Informs the user that the browser history has now been saved
        print(f"\nBrowser history has been saved to {output_file}")

    except sqlite3.Error as e:
        #Handles and SQLite errors
        print(f"SQLite error: {e}")

    finally:
        #Ensures the database connection is closed
        if connection:
            connection.close()

if __name__ == "__main__":
    #Asks user for path to chrome
    chrome_history_path = input("Enter the path to the Chrome history database: ")

    #Asks user for path to save output file
    output_file_path = input("Enter the path to save the output file (e.g., output.txt): ")

    #Calls the function to analyze chrome history and save results to output file
    analyze_chrome_history(chrome_history_path, output_file_path)
