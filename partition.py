class Solution:
    def partition(self, s):
        # mainArray = []

        # counter = 1

        # while counter < len(s):
        #     tempArray = []
        #     temp = ""
        #     for char in s:
        #         temp += char
        #         if len(temp) == counter and temp == temp[::-1]:
        #             tempArray.append(temp)
        #             temp = ""

        #     counter += 1
        #     mainArray.append(tempArray)
            


        # return mainArray

        self.ans = []
        ds = []
        self.solve(0, s, ds)
        return self.ans

    def solve(self, idx, s, ds):
        if idx == len(s):
            self.ans.append(ds[:])
            return
        
        for swi in range(idx, len(s)):
            if s[idx:swi+1] == s[idx:swi+1][::-1]:
                ds.append(s[idx:swi+1])
                self.solve(swi+1, s, ds)
                ds.pop()

        return

if __name__ == "__main__":
    obj = Solution()

    s = "aab"

    print(obj.partition(s))

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]