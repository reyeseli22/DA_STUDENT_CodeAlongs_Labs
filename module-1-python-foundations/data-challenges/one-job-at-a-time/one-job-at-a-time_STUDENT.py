#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "/Users/Marcy_Student/Documents/Marcy/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/one-job-at-a-time/pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    """Returns a verdict and a reason for one donation record"""
    parts = record.split(",")
    if len(parts) != 5:
        return (False, "wrong field count")
    if parts[2].strip() == "":
        return (False, "Missing Category")
    try: 
        float(parts[3])
    except ValueError:
        return (False, "pounds is not a number")
    return (True, "")



records = read_donations(DATA_FILE)
valid = []
for record in records:
    ok, reason = validate_donation(record)
    if ok:
        valid.append(record)
    else:
        print("REJECTED", record.split(",")[0]+":", reason)
print(len(valid), "usable records out of", len(records))
# Step 1, answer 1:
# One record or row holds donation_id ,item,category ,pounds , and received_on
# Step 1, answer 2:
# My validator promises to check that each record has 5 fields, 
# that the category is not empty, 
# and that the pounds field can be converted to a float. 
# If any of these checks fail, it returns False and a reason; otherwise, it returns True and an empty string.                                                  
print()

# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    """Calculates total lbs donated for each category."""
    by_category = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(",")
        category = parts[2]
        pounds = float(parts[3])
        if category not in by_category:
            by_category[category] = {"donations": 0, "pounds": 0.0}
            by_category[category]["donations"] += 1
            by_category[category]["pounds"] += pounds
            total_pounds += pounds
    return {"records": len(valid_records), "total_pounds": total_pounds, "by_category": by_category}
summary = summarize_donations(valid)
    
print("records:", summary["records"], "| total pounds:",
    summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"], "lbs")




# Step 2, answer 1:
# I hand counted grain, my result was 100 lbs total
# The printed line reflects 80 lbs of grain. One line was not counted because pounds was not an int


# ===== Day 2 =====
print()
# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    """Export the summary (dict) to a JSON file at the given path."""
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    return path
  
    
def run_pipeline(in_path, out_path, summarize):
    """Runs the pipeline to read, validate, summarize and export"""
    kept = []
    for items in read_donations(in_path):
        ok, reason = validate_donation(items)
        if ok:
            kept.append(items)
    return export_summary(summarize(kept), out_path)





written = run_pipeline(DATA_FILE, "donation_summary.json",summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations, export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])


# # Step 3, answer 1:
# print(len) gave us <built-in function len>
# print(len("abc")) gave us 3 
# Parenthesis are used to call a function and pass arguments through if necessary 
# Step 3, answer 2:
# Yes, the run_pipeline function needs and twice because it has to call the 3 functions we made previous to it

print()
# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    '''Calculates total pounds donated each day'''
    by_day = {}
    total_pounds = 0.0
    for record in valid_records:
            parts = record.split(",")
            day = parts[4]
            pounds = float(parts[3])
            if day not in by_day:
                by_day[day] = {"donations": 0, "pounds": 0.0}
            by_day[day]["donations"] += 1
            by_day[day]["pounds"] += pounds
            total_pounds += pounds
    return {"records": len(valid_records), "total_pounds": total_pounds, "by_day": by_day}
    

run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
with open("donation_summary.json") as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
    reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:
# I did not edit any other functions for the swap, 
# Step 4, answer 2:
# The 3 dates where only 1 donation is shown, 
# are instances where the other line was dropped because it did not pass validation.
