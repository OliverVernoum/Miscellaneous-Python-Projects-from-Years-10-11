import time
from datetime import datetime as d
import os


while True:
    # Get the current date and time
    now = d.now()
    
    # Format the date and time
    formatted_now = now.strftime("%d-%m-%Y %H:%M:%S")
    
    # Print the current date and time, overwriting the previous output
    print(f"Current date and time: {formatted_now}", end= '\r')
    os.system('cls')
    
    # Optional: Add a small delay (e.g., 1 second) to avoid overwhelming the terminal
    time.sleep(1)  # Adjust as needed to control the refresh rate
