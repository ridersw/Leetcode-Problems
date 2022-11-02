class Solution:
    def program(self, numbers):
        count = 0

        for swi in range(len(numbers)- 1):
            for swj in range(swi+1, len(numbers)-1):
                if len(str(numbers[swi])) == len(str(numbers[swj])):
                    temp_count = 0
                    num1 = str(numbers[swi])
                    num2 = str(numbers[swj])
                    for swk in range(len(str((numbers[swi])))):
                        if num1[swk] != num2[swk]:
                            temp_count += 1

                        if temp_count > 1:
                            break

                    if temp_count < 2:
                        count += 1
                # print(f'Num1: {numbers[swi]} and num2: {numbers[swj]}')

        return count

if __name__ == "__main__":
    obj = Solution()

    numbers = [1,151,241,1,9,22,351]

    print(obj.program(numbers))