#!/usr/bin/env python3
"""Day 4 code-along: Local vs. Global Variables & Scope. Run: python3 <file>"""

# ===== 1. Local Scope, Live =====
<<<<<<< HEAD
# Find out whether a variable made inside a function still exists outside of
# it.

# This is supposed to raise NameError: run it, read the traceback, then comment
# out the raising line so the rest of the file runs.
#
# DISCUSS: Before you run the Local Scope code, put these in the order they
#          happen. A: total stops existing. B: make_total() is called. C: total
#          is created and set to 100.
=======
# Find out if a variable made inside a function exists outside it.
# TODO: run it, read the NameError, then comment out the raising line
# DISCUSS: Order: A: total disappears. B: make_total() runs. C: total = 100.
>>>>>>> upstream
# Your answer:
#
print('----- 1. Local Scope, Live -----')
<<<<<<< HEAD
# TODO: define make_total() with a local variable total set
# to 100, returning it, then try printing total outside the
# function and watch what happens
def make_total():
    total = 100 
    return total
print(make_total())
# DISCUSS: Now try a new function. set_x() runs and sets x = 5 inside it, but
#          print(x) outside raises NameError. Why?
# Your answer: Because the code is using x = 5 doesnt exist where the code can see it 
=======
# TODO: define make_total(): set a local total to 100 and return it
# TODO: print total outside the function and see what happens

# DISCUSS: set_x() sets x = 5, but print(x) outside raises NameError. Why?
# Your answer:
>>>>>>> upstream
#


# ===== 2. Reading a Global, Live =====
<<<<<<< HEAD
# Work out the price of a $100 item with 8% tax, using a tax rate stored
# outside the function. 8% tax on $100 is $8. The total price will be $108
print('----- 2. Reading a Global, Live -----')
# TODO: define tax_rate as a global, then write
# price_with_tax(price) that reads it without taking it as
# a parameter
tax_rate = 0.08

def price_with_tax(price, c_tax_rate):
    return price + (price * c_tax_rate)
print(price_with_tax(20,tax_rate))


=======
# Price a $100 item with 8% tax, using a tax rate stored outside the function.
print('----- 2. Reading a Global, Live -----')
# TODO: define tax_rate as a global
# TODO: write price_with_tax(price) that reads tax_rate directly
>>>>>>> upstream

# DISCUSS: Move price_with_tax to a file with no tax_rate. Why does it break?
# Your answer:
#


# ===== 3. Refactor: Global to Parameter =====
<<<<<<< HEAD
# Pass the tax rate in as a parameter, so the function only uses what it is
# given. It should still print 108.0.
# print('----- 3. Refactor: Global to Parameter -----')
# TODO: rewrite price_with_tax so tax_rate is a parameter
# instead of a global it secretly reads
    #tax_rate = 0.08
=======
# Pass the tax rate in as a parameter. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
# TODO: rewrite price_with_tax to take tax_rate as a parameter
tax_rate = 0.08
>>>>>>> upstream
