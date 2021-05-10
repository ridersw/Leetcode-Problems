def maximumTime(time):
	
	hours, minutes = time.split(":")
	
	#print(f"hours: {hours}")
	#print(f"minutes: {minutes}")
	
	hours = list(hours)
	minutes = list(minutes)
	
	if '?' in hours:
		if hours[0] == '?' and hours[1] == '?':
			hours[0] = '2'
			hours[1] = '3'
		elif hours[0] == '?' and hours[1] < 4:
			hours[0] = '2'
		elif hours[0] == '?' and hours[1] >= 4:
			hours[0] = '1'
		elif hours[1] == '?' and int(hours[0]) < 2:
			hours[1] = '9'
		else:
			hours[1] = '3'
	
	if '?' in minutes:
		if minutes[0] == '?' and minutes[1] == '?':
			minutes[0] = '5'
			minutes[1] = '9'
		elif minutes[0] == '?':
			minutes[0] = '5'
		elif minutes[1] == '?':
			minutes[1] = '9'
	
	hours = "".join(hours)
	minutes = "".join(minutes)
	
	return hours + ":" + minutes
	
	#return time
	
	print(f"hours: {hours}")
	print(f"minutes: {minutes}")
	
	return str(hours + ":" + minutes)
	
if __name__ == "__main__":
	print(maximumTime("??:??"))
	print(maximumTime("2?:?0"))
	print(maximumTime("0?:3?"))
	print(maximumTime("1?:22"))
	print(maximumTime("00:01"))
	print(maximumTime("?4:03"))
	
#You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

#The valid times are those inclusively between 00:00 and 23:59.

#Return the latest valid time you can get from time by replacing the hidden digits.

#Example 1:

#Input: time = "2?:?0"
#Output: "23:50"
#Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
#Example 2:

#Input: time = "0?:3?"
#Output: "09:39"
#Example 3:

#Input: time = "1?:22"
#Output: "19:22"	