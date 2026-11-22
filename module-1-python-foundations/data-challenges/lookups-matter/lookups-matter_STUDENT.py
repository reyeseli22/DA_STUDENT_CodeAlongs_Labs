#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "/Users/Marcy_Student/Documents/Marcy/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/lookups-matter/member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "/Users/Marcy_Student/Documents/Marcy/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/lookups-matter/door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    comparisons = 0
    for row in members:
        comparisons += 1
        if row["member_id"] == member_id:
            return row,comparisons
    
    return None, comparisons



row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# I predict 150 for M1150, I got this by inferring that member_id increments by 1
# each id begins with 1 so M1150 shold be the 150th position


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`

with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()
    linear_total = 0
    not_members = 0
    
    for member_id in swipes:
        row,comparisons = find_linear(members,member_id)
        linear_total += comparisons
        if row is None:
            not_members += 1
            print(f"{member_id} | NOT A MEMBER | comparisons : {comparisons}")
        else:
            print(f"{member_id} | {row['name']} | comparisons: {comparisons}")

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)
print()
# Step 2, answer 1:
# The cost of the first 3 swipes would be 4, 12 and 27 and their sum would be 43 
# The cost for a non member would be 312
# Step 2, answer 2:
# The swipes for non_members cost the most, because we had to look through the entire dataset to verify their presence


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off

members_by_id = {}

build_steps = 0

for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1


def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1




print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))
linear_running = 0
dict_running = build_steps
pays_off_at = None
swipe_number = 0

print()

for member_id in swipes:
    swipe_number += 1

    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    linear_running += linear_count
    dict_running += dict_count  
    print(swipe_number, member_id, linear_running, dict_running)
    
    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number


print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# I predict the dict total will first drop below linear total at swipe 5
# Because line 6 in door checkins is M1313 that means it will cost 312 for that search, while dict will only add by 1
# Step 3, answer 2:
# A dict fit's the doors job because you can search by key to find the key value pair
# This is shown in swipe 6 M1313 574 318. this is the first instance where linear_running(574) becomes greater than dict_running(318)
# Step 3, answer 3:
# A morning where there were'nt many swipes a plain list would be the better choice.
# For example at swipe 5, linear search cost was still less than dict cost lookup.
# If there were a morning where only 5 swipes were recorded, the dict wouldnt be worth it.



ai_claim = """For a list of 312 rows, a linear search checks rows one at a time. A dict lookup uses a hash and takes about 1 step.
First lookup alone: it depends on where the ID sits. On average a linear search checks about 156 rows (half the list), so the dict is roughly 156x fewer steps. If the ID is near the front, the gap is much smaller.
ID not in the list: linear search must check all 312 rows, and the dict answers in 1 step, so about 312x.
All 20 lookups: about 20 x 156 = 3,120 linear steps versus 20 dict steps, so roughly 156x faster.
No. Those numbers compare only the lookups. Building the dict costs about 312 steps (one per row). Including that, the dict total is about 332 steps versus about 3,120 for linear, so the speedup for the whole morning is closer to 9x, not 156x."""
print("AI CLAIM:", ai_claim)



_, front_count = find_linear(members, swipes[0])
_, absent_count = find_linear(members,"M1313")
ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,"| ratio:", ratio)


verdict = """O(n) is the way find_linear grows, the work scales with the quantity of roles 
O(1) Average-Case is the way find_dict operates. One step per search
from lines 1 - 5 dict search consistently grows 1 step at time while linear search grows by the items position"""
print("VERDICT:", verdict)

# # Step 4, answer 1:
# A.I claims: All 20 lookups: about 20 x 156 = 3,120 linear steps versus 20 dict steps
# My results show linear: 2924 | dict: 332
# # Step 4, answer 2: 
# # No, its answer did not include the cost of the build. 
# # When I pasted my totals back heres the response:
"""""Your totals match what I predicted: linear 2924 and dict 332, which makes the ratio 2924 ÷ 332 = 8.8. The build cost is already inside the 332 (312 build + 20 lookups), so that is the fair whole-morning comparison.
Here's how your numbers line up against the AI's claims I wrote earlier:

"About 156x faster for all 20 lookups": your morning ratio is 8.8, so that claim is far too big for your data. It left out the 312-step build cost.
"About 9x once you include the build": this is almost exactly your 8.8. The small gap exists because I estimated linear at 3,120 steps using the average case, while your real morning cost 2924.
"312x for a non-member": this holds for your data. M1313 cost linear 312 steps against 1 for the dict.
"About 156 on average for the first lookup": your first swipe was M1004, which cost only 4, so the average-case claim doesn't describe that swipe at all."""