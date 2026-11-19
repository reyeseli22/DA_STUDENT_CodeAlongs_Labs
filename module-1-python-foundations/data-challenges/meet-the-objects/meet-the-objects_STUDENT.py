#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)

# 1. 
# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
# TODO: loop over `stations`; append each one's "name" to `names`
# TODO: append the same station's "bikes_available" to `bikes`
# names.pop(2)
names = []
bikes = []
for station in stations:
    names.append(station["name"])
    bikes.append(station["bikes_available"])
print("stations in the file:", len(stations))
print()
names.pop(2)
bikes.pop(2)
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")

# print()

# for i in range(len(stations)):
#     print(stations[i]["name"], stations[i]["bikes_available"])
# ^ Written to compare whats missing

# Step 1, answer 1:
# In the bike_stations.json each record is a dict containing station id, name, capacity, bikes available and needs maintenance 
# station id and name are str, capacity and bikes available are ints and needs maintenance is a bool. 
# The data is stored in a list of dicts.
# Step 1, answer 2:
# .pop(2) removes the value at the 2nd index
# Step 1, answer 3:
# No stations got a bike count that isnt theirs.
# Nobody sees the real count of w 52nd st and 11th ave, because we removed it with .pop(2) on names and bikes
print()

# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
    # TODO: in __init__, assign each parameter to self.<same name>
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    # TODO: add a parameter and self.<name> for each extra field you agreed
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
        return self.bikes_available < self.capacity/4


# TODO: assign `fleet` to []; loop over `stations` as `s`
fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
busy = fleet[1]
quiet = fleet[-1]

print(busy.name, busy.bikes_available, "of", busy.capacity)
print(quiet.name, quiet.bikes_available, "of", quiet.capacity)

print()
print("Before:",busy.needs_restock(), quiet.needs_restock())
print()
# TODO: print both needs_restock() answers
# TODO: set busy.bikes_available to 0, then print both answers again
busy.bikes_available = 0 
print(busy.name, busy.bikes_available, "of", busy.capacity)
print("After:",busy.needs_restock(), quiet.needs_restock())

# Step 2, answer 1:
# def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance)
# self.station_id = station_id
        # self.name = name
        # self.capacity = capacity
        # self.bikes_available = bikes_available
        # self.needs_maintenance = needs_maintenance
# Step 2, answer 2:
# Our two lists deffered in spellings and names, we kept my list as it seemed more industry standard.
# Step 2, answer 3:
#I did not leave any field from the file out, all are necessary to the dispatchers analysis
# Step 2, answer 4:
# Flatbush had 29 of 31 which is not inder the needs_restock threshold. 
# Amsterdam Ave had 33 of 25, again not meeting the needs_restock


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print()


class Station:
    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
    # TODO: in __init__, assign each parameter to self.<same name>
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    # TODO: add a parameter and self.<name> for each extra field you agreed
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
        return self.bikes_available < self.capacity/4
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"
fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))

print(fleet[0])
print(fleet[:2])
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()

# TODO: print both needs_restock() answers
# TODO: set busy.bikes_available to 0, then print both answers again




# TODO: copy your Station class from Step 2 here
# TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
# TODO: build it from self.name, self.bikes_available and self.capacity
# TODO: rebuild `fleet` from this class with the same loop as Step 2
print()
print(str(fleet[0]))
print(repr(fleet[0]))

# Step 3, answer 1:
# I expect: False False
#           True False
# Step 3, answer 2:
# No prediction was wrong, a list uses  __rpr__ instead of __str__

print()
# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# TODO: copy your Station class from Step 3 here   
# TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
# TODO: rebuild `fleet` from this class with the same loop as Step 2
# TODO: assign `van_list` to []; loop over `fleet`
# TODO: append each station whose needs_restock() returns True to `van_list`
class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity/4
    def __repr__(self):
        return f"Station({self.name!r}, {self.bikes_available})"
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"
fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))
van_list = []
for f in fleet:
    if f.needs_restock():
        van_list.append(f)

busy = fleet[1]
quiet = fleet[-1]
print("Before", busy.needs_restock(), quiet.needs_restock())
busy.bikes_available = 0 
print("After", busy.needs_restock(), quiet.needs_restock())

print(fleet[0])
print(fleet[:2])

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
# I predict 6 stations will land in van_list and print(van_list) will use __rpr__
# Step 4, answer 2:
#__rpr__ is used by programmers and developers and shows all syntax and how it was created
#__str__ is for layman readability and digestion
# Step 4, answer 3:
# I would hand the dispatcher the printout using __str__ because he is not a programmer and would benefit from the extra readability.
