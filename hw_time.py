import time
import sys

def print_timer(seconds):
    for i in range(seconds):
        print(f"Time elapsed: {i+1} seconds")
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <seconds>")
    else:
        try:
            seconds = int(sys.argv[1])
            print_timer(seconds)
        except ValueError:
            print("Error: Invalid input. Please provide an integer number of seconds.")
