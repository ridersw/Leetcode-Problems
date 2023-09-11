class Solution:
    def reverseWords(self, intervals):
        result = intervals.split()

        for swi in range(len(result)):
            result[swi] = result[swi][::-1]

        result = " ".join(result)
        return result


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.reverseWords("Hello World! OpenAI is amazing"))