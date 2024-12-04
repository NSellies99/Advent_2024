import csv
from heapq import heappop, heappush
import os
from pathlib import Path

location_file_path = Path(os.path.dirname(os.path.realpath(__file__))) / "locations.csv"


def distance_calculator():
    """Calculates the distance between the two location lists"""
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

def similarity_calculator():
    """Calculates the similarity score between the two location lists"""
    locations_one: list[int] = []
    locations_two: list[int] = []

    with open(location_file_path, mode="r") as location_file:
        location_reader = csv.reader(location_file)

        # Add both lists from CSV
        for line in location_reader:
            locations_one.append(int(line[0]))
            locations_two.append(int(line[1]))
        
        # Get the similarity score and add it to the total similarity
        similarity_score = 0
        for location in locations_one:
            similarity_score += location * locations_two.count(location)
        
        print(f"The total similarity score is {similarity_score}")

distance_calculator()
similarity_calculator()