


class Solution:
    def numberOfArithmeticSlices(self, nums):
        result = []

        eleCount = 3

        while eleCount <= len(nums):
            for swi in range(len(nums)-eleCount+1):
                print(f'nums[swi:eleCount]: {nums[swi:swi+eleCount]}')
                tempArr = []
                for swj in range(swi+1, swi+eleCount):
                    print(f'subtracting {nums[swi]} and {nums[swi-1]}')
                    tempArr.append(abs(nums[swj]-nums[swj-1]))
                print(f'tempArr: {tempArr} and tempArr: {tempArr} len(set(tempArr)): {len(set(tempArr))}')
                if len(set(tempArr)) == 1 and nums[swi:swi+eleCount] not in result:
                    result.append(nums[swi:swi+eleCount])


            eleCount += 1

        print(f'result: {result}')
        return len(result)


if __name__ == "__main__":
    obj = Solution()
    # print(obj.numberOfArithmeticSlices(nums = [1,2,3,4]))
    # print(obj.numberOfArithmeticSlices(nums = [1]))
    print(obj.numberOfArithmeticSlices(nums=[1,2,3,8,9,10]))