#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
# TODO: assign `EXPECTED_FIELDS` to 5
EXPECTED_FIELDS = 5
# TODO: assign `ALLOWED_STATUS` to ["Open", "In Progress", "Closed"]
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]

# TODO: assign `fields` to `row` split on commas
# TODO: unpack `fields` into the five names in the CSV header
# TODO: if `borough` is empty, return False and "borough is empty"
# TODO: if `status` is not in ALLOWED_STATUS, return False and a reason
# TODO: return True and "ok"
def validate_request(row):
    fields = row.split(",") 
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    request_id, complaint_type, borough, days_open, status = fields
    if borough == "":
        return False, "borough is empty"
    if status not in ALLOWED_STATUS:
        return False, "status not allowed: " + status
    return True, "ok"


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))
print()
# Step 1, answer 1:
# In the file there are 15 rows of data, Eaxh row is split into 5 columns, the headers are as follows request_id, complaint_type, borough, days_open, status. 
# Upon initial obsevation I see there are 3 rows that are invalid, 
# the first row is valid, the second row has an empty borough field and the third row has a status that is not allowed.
# Step 1, answer 2: 
# return a and b ; it returns a tuple of two values, 
# the first is a boolean indicating if the request is valid, and the second is a string providing the reason for rejection or "ok" if valid.
#


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
# TODO: assign `valid` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if `ok`, add 1 to `valid`
# TODO: else print row.split(",")[0], "REJECTED -" and `reason`
valid = 0 
for row in rows:
    ok, reason = validate_request(row)
    if ok:
        valid += 1
    else:
        print(row.split(",")[0], "REJECTED -", reason)
print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)
print()
# Step 2, answer 1:
# 3 rows fail. The rows and the reason they failed are as follows
# SR-1004 REJECTED -borough is empty
# SR-1009 REJECTED -status not allowed: Escalated
# SR-1011 REJECTED -wrong field count: 4
# Step 2, answer 2:
# The line below should not have passed, the amount of days the request has been open says -3 days
# SR-1013,Sidewalk Condition,Manhattan,-3,Open
# The line below should not have passed, the days_open states "3 days" a str not an int
# SR-1014,Illegal Parking,Staten Island,7,Closed
print()
# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
# TODO: assign `total_days` and `counted` to 0
# TODO: loop over `rows`; `continue` past any row validate_request() rejects
# TODO: assign `days_open` to int() of the row's fourth field
# TODO: add `days_open` to `total_days` and 1 to `counted`
# TODO: print the row's ID, "days open:" and `days_open`
# TODO: after your answers, comment out this step so Step 4 can run

# print("average days open:", total_days / counted) 
total_days = 0
counted = 0
try:
    for row in rows: 
        ok, reason = validate_request(row)
        if not ok:
            continue 
    days_open = int(row.split(",")[3])
    total_days += days_open
    counted += 1 
    print(row.split(",")[0],"days open:", days_open)
except:
    e = ValueError
    print("Error processing row:", row)
print("average days open:", total_days / counted)

# Step 3, answer 1:
# I predict 6 report lines will print before it crashes. 
# The first 6 rows contain int in the [3] field, the 7th contains a str

# Step 3, answer 2:
#Traceback (most recent call last):
#   File "/Users/Marcy_Student/Documents/Marcy/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/validate-catch-keep-going/validate-catch-keep-going_STUDENT.py", line 95, in <module>
#     days_open = int(row.split(",")[3])
# ValueError: invalid literal for int() with base 10: '3 days'
# No rows were counted before 

# Step 3, answer 3:
# They were ignored



# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    total_days = 0
    counted = 0
try:
    for row in rows: 
        ok, reason = validate_request(row)
        if not ok:
            continue 
    days_open = int(row.split(",")[3])
    total_days += days_open
    counted += 1 
    print(row.split(",")[0],"days open:", days_open)
except:
    e = ValueError

    # TODO: in a try, assign `days` to int(value)
    # TODO: in except ValueError, return False and a reason
    # TODO: make that reason "days_open is not a number: " plus `value`
    # TODO: if `days` is below 0, return False and a reason
    # TODO: make that reason "days_open is negative: " plus `value`
    # TODO: return True and "ok"



# TODO: assign `total_days`, `counted` and `skipped` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if ok, unpack check_days_open() of the fourth field into ok, reason
# TODO: if still ok, add the days to `total_days` and 1 to `counted`
# TODO: else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`

# print("counted:", counted, "| skipped:", skipped)
# print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
