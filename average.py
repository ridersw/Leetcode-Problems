class Solution:
    def average(self, salary):
        print(f'sum(salary): {sum(salary)}')
        print(f'min(salary): {min(salary)}')
        print(f'max(salary): {max(salary)}')
        print(f'len(salary): {len(salary)}')
        return (sum(salary)-min(salary)-max(salary)) / (len(salary)-2)


if __name__ == "__main__":
    obj = Solution()

    print(obj.average(salary = [4000,3000,1000,2000]))