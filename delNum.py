class Solution:
    def delNum(self, num):
        arr = []

        num = list(str(num))

        for swi in range(len(num)):
            if num[swi] == '5':
                temp = num[:swi] + num[swi+1:]
                temp = "".join(temp)
                temp = int(temp)
                arr.append(temp)

        # for swi in range(len(arr)):
        #     arr[swi] = int(arr[swi])

        arr.sort()
        return arr[-1]

if __name__ == "__main__":
    obj = Solution()

    print(obj.delNum(-5000))