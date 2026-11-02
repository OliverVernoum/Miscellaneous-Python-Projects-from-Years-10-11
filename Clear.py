import os
import sys

def clear_terminal():
    # Check if running in IDLE
    if "idlelib" in sys.modules:
        print("\n" * 100)  # Push previous content out of view
    else:
        # Regular terminal clearing
        os.system('cls' if os.name == 'nt' else 'clear')

# Example use
clear_terminal()
print("Hello, fresh terminal (or IDLE)!")
