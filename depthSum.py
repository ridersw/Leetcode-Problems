
class Solution:
    def depthSum(self, nestedList):

        result = 0
        temp_Arr = []
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        braces = ['[',']']

        nestedList = list(str(nestedList))

        print(f'nestedList: {nestedList}')
        totalCount = 0

        for ele in nestedList:
            if ele not in numbers and ele not in braces:
                nestedList.remove(ele)

        print(f'nestedList: {nestedList}')

        for ele in nestedList:
            if ele == " ":
                nestedList.remove(ele)

        print(f'nestedList: {nestedList}')

        for swi in range(len(nestedList)):
            if nestedList[swi] in numbers:
                result = result + (int(nestedList[swi]) * totalCount)
            elif nestedList[swi] == '[':
                totalCount += 1
            else:
                totalCount -= 1

        return result


if __name__ == "__main__":
    obj = Solution()
    
    nestedList = [[1,1],2,[1,1]]
    nestedList = [1,[4,[6]]]
    nestedList = [[1,1],2,[1,1]]

    print(obj.depthSum(nestedList))

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

 

# Example 1:


# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
# Example 2:


# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
# Example 3:

# Input: nestedList = [0]
# Output: 0
 

# Constraints:

# 1 <= nestedList.length <= 50
# The values of the integers in the nested list is in the range [-100, 100].
# The maximum depth of any integer is less than or equal to 50.