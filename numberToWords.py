class Solution:
    def numberToWords(self, num):

        if num == 0:
            return "Zero"

        self.ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand ", "Million ", "Billion "]

        res = ""

        
        tempNum = str(num)
        tempList = []

        while num > 0:
            tempList.insert(0, num % 1000)
            num //= 1000

        words = []

        for swi, segment in enumerate (tempList):
            segment_word = self.helper(segment)
            if segment_word:
                if self.thousands[len(tempList) - swi - 1]:
                    segment_word += " " + self.thousands[len(tempList) - swi -1]
                words.append(segment_word)

        return "".join(words).strip()
    
    def helper(self, num):
        if num == 0:
            return ""
        elif num < 10:
            return self.ones[num]
        elif num < 20:
            return self.teens[num - 10]
        elif num < 100:
            return self.tens[num // 10] + " " + self.ones[num %10]
        else:
            return self.ones[num // 100] + " Hundred " + self.helper(num%100).strip()



if __name__ == "__main__":
    obj = Solution()

    print(obj.numberToWords(num = 123))
    print(obj.numberToWords(num = 12345))
    print(obj.numberToWords(num = 1234567))