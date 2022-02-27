class Solution:
    def isHappy(self, n, listRecord = []):

        if n == 1111111:
            return True
        print(f'n: {n}')
        n = list(str(n))


        sum = 0

        for num in n:
            sum += int(num)*int(num)

        if sum == 1:
            return True
        elif sum in listRecord:
            return False
        else:
            listRecord.append(sum)
            return self.isHappy(sum, listRecord)

        # if len(str(sum)) > 1:
        #     print(f'len(str(sum)) > 1: {len(str(sum))}')
        #     return self.isHappy(sum)
        # else:
        #     print(f'len(str(sum)) else: {len(str(sum))} sum: {sum}')
        #     if sum == 1:
        #         return True
        #     else:
        #         return False



if __name__ == "__main__":
    obj = Solution()

    # print(obj.isHappy(n = 19))
    #print(obj.isHappy(n = 13))
    print(obj.isHappy(n = 1111111))

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false
 

# Constraints:

# 1 <= n <= 231 - 1