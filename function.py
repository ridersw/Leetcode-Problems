class Solution:
    def function(self, num):
        num = str(num)
    # sort the string
        s = sorted(num)
    
        # check for leading zero in string
        # if there are any leading zeroes,
        # swap the first zero with first non-zero number
        i = 0
        while (s[i] == '0'):
            i += 1
        a = list(s)
        temp = a[0]
        a[0] = a[i]
        a[i] = temp
        s = "".join(a)
        return s


if __name__ == "__main__":
    obj = Solution()
    print(obj.function(num = '320002'))

# get the minimum number from permutation of given number provided 0 does not take first position