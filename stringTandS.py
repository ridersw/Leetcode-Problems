class Solution:
    def program(self, t, s):
        if len(t) < 5:
            return 0

        count = 0
        s = list(s)

        for swi in range(len(t)-4):
            if t[swi] == s[0] and t[swi+2] == s[1] and t[swi+4] == s[2]:
                count += 1

        return count

if __name__ == "__main__":
    obj = Solution()

    t = "azcabcab"
    s = "acb"

    print(obj.program(t, s))