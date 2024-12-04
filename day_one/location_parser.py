import csv
from heapq import heappop, heappush
import os
from pathlib import Path

location_file_path = Path(os.path.dirname(os.path.realpath(__file__))) / "locations.csv"

locations_one: list[int] = []
locations_two: list[int] = []

with open(location_file_path, mode="r") as location_file:
    location_reader = csv.reader(location_file)

    # Add both lists from CSV as a heap
    for line in location_reader:
        heappush(locations_one, int(line[0]))
        heappush(locations_two, int(line[1]))        

    # Calculate total distance
    total_distance = 0
    for _ in range(len(locations_one)):
        location_one, location_two = heappop(locations_one), heappop(locations_two)
        total_distance += abs(location_one - location_two)

    print(f"The total distance is {total_distance}")