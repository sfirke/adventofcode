import numpy as np
import pandas as pd
dat = pd.read_csv("day1.txt", squeeze = True, names = "x")
fuel_needed = sum(np.floor(dat / 3) - 2)
fuel_needed
# It works with the sample input??
fuel_needed = np.floor(100756/3) - 2
fuel_needed
# fuel_needed = np.floor(1969/3) - 2
# fuel_needed


to_acct_for = np.floor(fuel_needed / 3) - 2
while to_acct_for > 0:
    print(to_acct_for)
    print(fuel_needed)
    fuel_needed = fuel_needed + to_acct_for
    to_acct_for = max(np.floor(to_acct_for / 3) - 2, 0)


fuel_needed
to_acct_for

# too high: 4943265
# too low:  3844754 - was double-shrinking the first one
# too high: 4943262