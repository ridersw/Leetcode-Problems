from re import L


class Solution:
    def multiples3or5(self, number):
        res = 0

        for swi in range(number):
            if swi % 5 == 0 or swi % 3 == 0:
                res += swi

        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.multiples3or5(1000))