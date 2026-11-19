#!/usr/bin/env python3
"""Day 19 code-along: Final Practice Gauntlet. Run: python3 <file>"""

# ===== 1. A Tool Class =====
# Write a Tool class with a name, a count, and is_low().
print('----- 1. A Tool Class -----')
# TODO: define a Tool class with a one-line docstring
class Tools:
    def __init__(self, name, count):
        self.name = name 
        self.count = count
    def is_low(self):
        if self.count <= 1:
            return True
    def __repr__(self):    # dunder repr, returns information to programmers 
        return f"Tool({self.name},{self.count})"
# passed values into tools and recreated an object called drill, and again for saw 
drill = Tools("drill", 1)
saw = Tools("saw", 4)
print(drill)
print(drill.is_low())
print(saw.is_low())





# TODO: __init__(self, name, count) stores both as attributes
# TODO: is_low(self) returns True when count is 1 or less
# TODO: __repr__(self) returns Tool('drill', 1) style text


# TODO: make drill = Tool("drill", 1) and saw = Tool("saw", 4)
# TODO: print drill, then drill.is_low() and saw.is_low()

# PREDICT before you run: With no __str__, what does print(drill) show?
# Your answer: print drill will print Tools("drill", 1)
# 
# DISCUSS: Why a class, not three parallel lists?
# Your answer:
#


# ===== 2. Check One Line =====
# Return a line's fields if valid; print why and return None if not.
print('----- 2. Check One Line -----')
FIELDS = {"ADD": 3, "LEND": 2}

def check_line(line):
    '''Validate each line and return reason, or NONE'''
    parts = line.strip().split(",")
    command = parts[0].upper()
    if command not in FIELDS:
        print(f"Skipped: unknown command {parts[0]}")
        return None
    if len(parts) != FIELDS[command]:
        print(f"Skipped: {command} needs {FIELDS[command]} fields")
    parts[0] = command
    if command == "ADD":
        try:
            parts[1] = int(parts[1])
        except ValueError:
            print(f"Skipped: count {parts[1]} is not a number")
            return None
        return parts
    


# TODO: split the stripped line on commas; uppercase the command
# TODO: unknown command? print why and return None
# TODO: wrong field count for that command? print why, return None
# TODO: for ADD, convert the count with int() inside try/except
# TODO: return the fields list when every check passes


for line in ["add,drill,2", "LEND,saw", "ADD,saw", "ADD,saw,two", "FIX,drill"]:
    print(check_line(line))

# PREDICT before you run: Which of the five lines come back as None?
# Your answer:
#
# DISCUSS: Why check field count before calling int()?
# Your answer:
#


# ===== 3. Build the Shelf =====
# Build a dict of Tool objects: ADD creates or restocks, LEND lends one.
print('----- 3. Build the Shelf -----')
# TODO: define apply_lines(lines) with a one-line docstring
# TODO: start an empty dict, tools; loop over lines with check_line
# TODO: skip a line that check_line returned None for
# TODO: ADD: restock if the name is in tools, else make a new Tool
# TODO: LEND: skip with a message if missing or count is 0
# TODO: otherwise subtract 1; return tools at the end


# lines = ["ADD,drill,2", "ADD,saw,1", "add,drill,1",
#          "LEND,saw", "LEND,saw", "LEND,ladder"]
# tools = apply_lines(lines)
# print(tools)

# PREDICT before you run: What are drill's and saw's counts at the end?
# Your answer:
#
# DISCUSS: Why key the dict by name instead of a list?
# Your answer:
#


# ===== 4. Save to JSON =====
# Write every Tool to tools.json as a list of dicts.
print('----- 4. Save to JSON -----')
import json


# TODO: define save_json(tools, path) with a one-line docstring
# TODO: turn each Tool in tools.values() into a dict, in a list
# TODO: write the list to path with json.dump(..., indent=2)
# TODO: return how many rows were written


# print(save_json(tools, "tools.json"))
# with open("tools.json") as f:
#     print(json.load(f))

# DISCUSS: Why can't json.dump() take the Tool objects as is?
# Your answer:
#
