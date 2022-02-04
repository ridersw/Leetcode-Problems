class Solution:
    def isPrime(self, number):
        if number == 2 or number == 3:
            return True

        if number <= 2:
            return False

        if number % 2 == 0 or number % 3 == 0:
            return False

        for swi in range(3, int(number * 0.5), 2):
            if number % swi == 0:
                return False

        return True 



if __name__ == "__main__":
    obj = Solution()

    print(obj.isPrime(12))
    print(obj.isPrime(11))
    print(obj.isPrime(17))

    print(obj.isPrime(1000000000000000000000098989733647267447863274678263486326478326486238467283648))