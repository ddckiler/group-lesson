import requests

import time

def get_iss_position():

  url = "http://api.open-notify.org/iss-now.json"

  response = requests.get(url)

  data = response.json()

  return data["iss_position"]["latitude"], data["iss_position"]["longitude"]

def main():

  csv_file = "iss_positions.csv"

  while True:

    latitude, longitude = get_iss_position()

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(csv_file, mode="a", newline="") as file:

      writer = csv.writer(file, delimiter=";")

      writer.writerow([timestamp, latitude, longitude])

    time.sleep(5)

if __name__ == "__main__":

  main()