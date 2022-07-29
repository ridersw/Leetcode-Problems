from typing import final


class Solution:
    def problem(self, inputString):
        skip = ['(',')',' ']
        operator = ['-', '+']
        ignore = ['_']
        finalString = []
        temp = ""

        for item in inputString:
            if item in skip:
                if temp:
                    finalString.append(temp)
                temp = ""
            elif item in operator:
                if temp:
                    finalString.append(temp)
                finalString.append(item)
                temp = ""
            else:
                temp += item

        if temp:
            finalString.append(temp)

        # print(f'finalString: {finalString}')

        if finalString[-1] == '+' or finalString[-1] == '-1':
            return "Invalid String"

        for swi in range(1, len(finalString)):
            if finalString[swi] in operator and finalString[swi-1] in operator:
                if finalString[swi] == '-' and finalString[swi-1] == '-':
                    finalString[swi-1] = '+'
                    finalString[swi] = ''
                elif finalString[swi] == '-' and finalString[swi-1] == '+':
                    finalString[swi-1] = '-'
                    finalString[swi] = ''
                elif finalString[swi] == '+' and finalString[swi-1] == '+':
                    finalString[swi-1] = '+'
                    finalString[swi] = ''
                else:
                    finalString[swi-1] = '-'
                    finalString[swi] = ''

        # print(f'finalString: {finalString}')

        for item in finalString:
            if item == "":
                finalString.remove(item)

        # print(f'finalString: {finalString}')

        if finalString[0] == '-':
            finalString = finalString[1:]
            finalString[0] = str(-int(finalString[0]))
            # print(f'finalString Line : {finalString}')
        elif finalString[0] == '+':
            finalString = finalString[1:]
            # print(f'finalString: {finalString}')

        if finalString[-1] == '+' or finalString[-1] == '-':
            return "Invalid String"


        ans = int(finalString[0])

        for swi in range(1,len(finalString), 2):
            if finalString[swi] == '+':
                ans += int(finalString[swi+1])
            else:
                ans -= int(finalString[swi+1])

        # print(f'ans: {ans}')

        return str(ans)


if __name__ == "__main__":
    obj = Solution()
    print(obj.problem(inputString = '200 + ((-100500 + 10000) + 2000)') == '-88300')
    print(obj.problem(inputString = '-200 + ((-100500 + 10000) + 2000)') == '-88700')
    print(obj.problem(inputString = '200 + ((-100_500 + 100_00) + 20_00)') == '-88300')
    print(obj.problem(inputString = '200 + ((-100_500 + 100_00) + 20_00 + )'))
    print(obj.problem(inputString = '- 200 + ((-100_500 + 100_00) + 20_00)') == '-88700')