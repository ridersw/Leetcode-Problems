class Solution:
    def groupAnagrams(self, strings):
        
        res = []

        for swi, word in enumerate(strings):
            doneLetters = []
            temp = ""
            for char in strings[swi]:
                if char not in doneLetters:
                    temp += str(strings[swi].count(char)) + char

            temp = list(temp)
            temp.sort()
            temp = "".join(temp)
            res.append([swi, temp])
        # print(f'strings: {strings}')
        # print(f'res: {res}')

        res.sort(key=lambda x:x[1])

        print(f'res: {int(res[0][0])}')
        ind = int(res[0][0])
        ref = res[0][1]
        print(f'ref: {ref}')
        temp = []
        print(f'temp: {temp}')
        answer = []
        for swi in range(len(res)):
            if res[swi][1] == ref:
                temp.append(strings[int(res[swi][0])])
                print(f'temp: {strings[int(res[swi][0])]}')
            else:
                if temp:
                    answer.append(temp)
                    temp = [strings[int(res[swi][0])]]
                    ref = res[swi][1]

        if temp:
            answer.append(temp)
        
        print(f'answer: {answer}')

        return answer


        # d = {}
        
        # for w in sorted(strings):
        #     key = tuple(sorted(w))
        #     d[key] = d.get(key, []) + [w]
            
        # return d.values()
            


if __name__ == "__main__":
    obj = Solution()

    print(obj.groupAnagrams(strings = ["eat","tea","tan","ate","nat","bat"]))

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.