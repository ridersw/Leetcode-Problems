class Solution:
    def program(self, candies):
        count_of_candies = 0

        left = 0
        right = len(candies)-1

        alice = bob = 0

        while left < right:
            while candies[left] == 0 and left + 1 < right:
                left += 1

            if candies[left] != 0 and right > left:
                alice += candies[left]
                count_of_candies += 1
            if self.checkBobAlice(bob, alice):
                return count_of_candies
            left += 1

            while candies[right] == 0 and right - 1 > left:
                right -= 1

            if candies[right] != 0 and right > left:
                bob += candies[right]
                count_of_candies += 1

            if self.checkBobAlice(bob, alice):
                return count_of_candies
            right -= 1

        return 0

    def checkBobAlice(self, bob, alice):
        if bob == alice:
            return True
        return False

if __name__ == "__main__":
    obj = Solution()

    candies = [1,2,1]

    print(obj.program(candies))