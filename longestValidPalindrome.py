class Solution:
    def longestValidPalindrome(self, s):

        stack, currLongest, maxLongest = [], 0, 0

        for char in s:
            if char == "(":
                stack.append(currLongest)
                currLongest = 0
            elif char == ")":
                if stack:
                    currLongest += stack.pop() + 2
                    maxLongest = max(currLongest, maxLongest)
                else:
                    currLongest = 0
        return maxLongest

            




if __name__ == "__main__":
    obj = Solution()

    s = ["(()", ")()())", ")(", "()(()"]

    for input in s:

        print(f'Answer: {obj.longestValidPalindrome(input)}')