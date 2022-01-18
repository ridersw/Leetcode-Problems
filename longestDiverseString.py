class Solution:
    def longestDiverseString(self, a, b, c):
        s = [[a,'a'],[b,'b'],[c, 'c']]
        ans = []

        print(f's: {s}')

        while True:
            s.sort()
            if len(ans) >= 2 and ans[-2] == ans[-1] == s[2][1]:
                swi = 1
            else:
                swi = 2

            if s[swi][0]:
                ans.append(s[swi][1])
                s[swi][0] -= 1
            else:
                break
        
        return "".join(ans)


        
if __name__ == "__main__":
    obj = Solution()

    a = 1
    b = 1
    c = 7

    print(obj.longestDiverseString(a, b, c))