from datetime import date

def dayOfTheWeek(day, month, year):
	return date(year,month,day).strftime("%A")
	
if __name__ == "__main__":
	day = 31
	month = 8
	year = 2019
	print(dayOfTheWeek(day, month, year))
	
#Given a date, return the corresponding day of the week for that date.

#The input is given as three integers representing the day, month and year respectively.

#Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

#Example 1:

#Input: day = 31, month = 8, year = 2019
#Output: "Saturday"
#Example 2:

#Input: day = 18, month = 7, year = 1999
#Output: "Sunday"