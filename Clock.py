from datetime import datetime as d
import time
import sys


while True:
    now = d.now()
    formatted_now = now.strftime('%Y-%m-%d %I:%M:%S')# Format the date and time
    print(f"Current date and time: {formatted_now}", end ='\r')
    

   



