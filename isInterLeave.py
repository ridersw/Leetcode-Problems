class Solution:
    def isInterleave(self, s1, s2, s3):
        pointer1, pointer2, pointer3 = 0,0,0 

        while pointer1 < len(s1) or pointer2 < len(s2) and pointer3 < len(s3):
            print(f'Checking for Character: {s3[pointer3]} at location: {pointer3} s1: {s1[pointer1:]} s2: {s2[pointer2:]}')
            if pointer1 < len(s1) and s1[pointer1] == s3[pointer3]:
                print(f'Character ')
                pointer1 += 1
                pointer3 += 1
            elif pointer2 < len(s2) and s2[pointer2] == s3[pointer3]:
                pointer2 += 1
                pointer3 += 1
            else:
                return False

        return True

if __name__ == "__main__":
    obj = Solution()

    print(obj.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))

    