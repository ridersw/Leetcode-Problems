class Solution:
    def findTheDifference(self, s, t):
        
        dict = {}
        
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
                
        for char in t:
            if char not in dict or dict[char] == 0:
                return char
            else:
                dict[char] -= 1

if __name__ == "__main__":
    obj = Solution()

    print(obj.findTheDifference(s = "abcd", t = "abcde"))