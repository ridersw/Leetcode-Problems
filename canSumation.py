class Solution:
    def canSum(self, arr, target, memo = {}):

        if target == 0:
            return []

        if target < 0:
            return None

        answer = []

        if target in memo:
            return memo[target]

        for num in arr:
            remainder = target - num
            remain = self.canSum(arr, remainder)

            if remain is not None:
                remain.append(num)
                if len(remain) < len(answer) or not answer:
                    answer = remain[:]

        return answer



if __name__ == "__main__":
    obj = Solution()

    arr = [2,5]
    target = 10

    print(obj.canSum(arr, target))