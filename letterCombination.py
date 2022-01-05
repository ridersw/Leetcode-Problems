class Solution:
    def letterCombination(self, digits):
        letters = ['', '',['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        if len(digits) == 1:
            return letters[int(digits)]

        if not digits:
            return []

        combination = letters[int(digits[0])]

        print(f'combination: {combination}')

        for swi in range(1, len(digits)):
            print(digits[swi])
            temp = digits[int(swi)]
            list1 = letters[int(temp)]
            list2 = combination[:]


            # print(f'list1: {list1}')
            # print(f'list2: {list2}')

            len1 = len(list1)
            len2 = len(list2)

            for swj in range(len1):
                for swk in range(len2):
                    temp = list1[swj] + list2[swk]
                    combination.append(temp)

        combination.sort(key = len)
        # print(f'combination: {combination}')
        print(f'len(combination): {len(combination)}')

        if len(digits) == 2:
            res = []

            for char in combination:
                if len(char) == 2 and char not in res:
                    res.append(char)

            return res

        elif len(digits) == 3:
            res = []

            for char in combination:
                if len(char) == 3 and char not in res:
                    res.append(char)

            return res
        else:
            res = []

            for char in combination:
                if len(char) == 4 and char not in res:
                    res.append(char)

            return res

if __name__ == "__main__":
    obj = Solution()

    digits = "999"

    output = ["www","wwx","wwy","wwz","wxw","wxx","wxy","wxz","wyw","wyx","wyy","wyz","wzw","wzx","wzy","wzz","xww","xwx","xwy","xwz","xxw","xxx","xxy","xxz","xyw","xyx","xyy","xyz","xzw","xzx","xzy","xzz","yww","ywx","ywy","ywz","yxw","yxx","yxy","yxz","yyw","yyx","yyy","yyz","yzw","yzx","yzy","yzz","zww","zwx","zwy","zwz","zxw","zxx","zxy","zxz","zyw","zyx","zyy","zyz","zzw","zzx","zzy","zzz"]

    print(obj.letterCombination(digits) == output)

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
    