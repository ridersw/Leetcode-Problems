class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30
        
        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
        
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360- diff)

if __name__ == "__main__":
    obj = Solution()

    print(obj.angleClock(hour = 12, minutes = 30) == 165.0)
    print(obj.angleClock(hour = 3, minutes = 30) == 75.0)
    print(obj.angleClock(hour = 3, minutes = 15) == 7.5)
    print(obj.angleClock(hour = 11, minutes = 22) == 151.00000)

# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

# Answers within 10-5 of the actual value will be accepted as correct.

 

# Example 1:


# Input: hour = 12, minutes = 30
# Output: 165
# Example 2:


# Input: hour = 3, minutes = 30
# Output: 75
# Example 3:


# Input: hour = 3, minutes = 15
# Output: 7.5
 

# Constraints:

# 1 <= hour <= 12
# 0 <= minutes <= 59