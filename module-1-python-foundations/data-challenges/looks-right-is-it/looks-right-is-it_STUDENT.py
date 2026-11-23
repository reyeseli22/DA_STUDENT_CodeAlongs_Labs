#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "/Users/Marcy_Student/Documents/Marcy/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/looks-right-is-it/timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()



# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(); run again
# TODO: find that printed value in the CSV
# TODO: fix the line that reads the wrong column to read the hours column
# TODO: wrap that value in int() so add_hours() adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right
def add_hours(total, hours):
    print(repr(hours))
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total,int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))
print()
# Step 1, answer 1:
# Rosa's[E101] weekly hours add up to 40 total
# Step 1, answer 2:
# To read a trace back:
# First: You start with the bottom line, this is what tells you the type of error and the message
# Second: we look at the line above which will indicate what line is causing the error
# Lastly, we continue to scroll up to see if there are any additional error messages and continiue the process
# Step 1, answer 3:
# The trace_back ended in the add_hours function,
# line 30, in weekly_hours total = add_hours(total,parts[3]) was the bug.


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# TODO: run the file as given; note the last ID that printed
# E103 was the last ID to print before the error "E103 | hours: 32 | days: 5 | average per day: 6.4"
# 5 unique employee names are in the csv
# E106 is present in the staff list, no such employee_id is present in csv
# TODO: compare every ID in `staff` with the IDs in the CSV
# TODO: replace the hand-typed `staff` list with an empty list
# TODO: loop over lines[1:]; append each row's employee ID to `staff` once
# TODO: print "employees in the file:" and len(staff)
def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days


staff = []

for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,"| average per day:", hours / days)
print()
for row in lines[1:]:
    parts = row.split(",")
    emp_id = parts[0]
    if emp_id not in staff:
        staff.append(emp_id)
print("Employees in staff :", len(staff))
# Step 2, answer 1:
# There are 5 employees in the csv
# Step 2, answer 2:
# It stopped on E103
# Step 2, answer 3:
# The bug lied inside the staff list, with the value that didn't exist in the csv


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# TODO: add up Rosa's (E101) and Mei's (E103) hours by hand first
# (By Hand Totals)
# Rosa's hours (E101): 40 
# Mei's hours (E103): 32
# TODO: print("starting", emp, "total is", total) first in the outer loop
# TODO: move the line that sets `total` inside the outer loop
# TODO: delete the "starting" print once all five totals are right

records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})

employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])


for emp in employee_ids:
    total = 0 
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)
print()
# Step 3, answer 1:
# Rosa's hours (E101): 40 
# Mei's hours (E103): 32
# Step 3, answer 2:
# total initially held the running total for hours across all employees when it was outside of the outer-loop
# when we moved it into the outer loop, it held 0 at the start of each employee count
# The placement of Total = 0 explains it
# Step 3, answer 3:
# Rosa's number is right because her's was the first iteration, with total = 0 outside of the loop
# and priya being the last employee in the list, her totals would equal the whole staff's, because the count never reset to 0 for every employee


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's, Darnell's and Mei's pay by hand first
# Rosa's (E101) pay: 40 hrs : $24/hr : $960 x 3 = $2,880
# Darnell's (E102) pay: 46 hrs(6hrs OT): Base:$31.50 OT:$47.25 : (Base Pay): $1,260 (OT Pay):$283.50 Total: $1543.50 x 3 = Base:$3,780 OT: $850 Total: $4,630
# Mei's (E103) pay: 32 hrs: $28/hr : $896 x 3 = $2,688
# TODO: fix weekly_pay() so it follows the handbook rule word for word
# TODO: fix the other line that compares `total` against 40 the same way
def weekly_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        return 40 * rate + overtime_hours * rate * 1.5
    return hours * rate 


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total > 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")
print()
# Step 4, answer 1:
# Rosa's (E101) pay: 40 hrs : $24/hr : $960 
# Darnell's (E102) pay: 46 hrs(6hrs OT): Base:$31.50 OT:$47.25 : (Base Pay): $1,260 (OT Pay):$283.50 Total: $1543.50
# Mei's (E103) pay: 32 hrs: $28/hr : $896
# Step 4, answer 2:
# I found 3 bugs
# 1 & 2: weekly_pay had if hours >= 40 which includes 40 hour totals in overtime, when the rule is over 40 hours not 40 hours or over
# I changed it to if hours/total > 40 
# 3. weekly_pay made it so if hours was over 40 then all hours would be 1.5 x Rate
# It should be 1.5x the hours over 40, I added overtime_hours = hours - 40
        # return 40 * rate + overtime_hours * rate * 1.5   so that if over 40 the amount of hours over 40 would be 1.5x the rate
# Step 4, answer 3:
# Rosa's exactly-40 week can spot the bug, because we know she does not fit the hours criteria to get overtime, as she has exactly 40 hours not over as specified in the handbook rule
