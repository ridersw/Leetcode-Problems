from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        days1 = datetime.strptime(date1, '%Y-%m-%d').date()
        days2 = datetime.strptime(date2, '%Y-%m-%d').date()

        return abs((days1 - days2).days)

# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

# Example 1:

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:

# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
 

# Constraints:

# The given dates are valid dates between the years 1971 and 2100.