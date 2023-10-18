class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if not p:
            return not s
        
        first_character = bool(s) and (s[0] == p[0] or p[0] == ".")

        if len(p) >= 2 and p[1] == "*":
            return (first_character and self.isMatch(s[1:],p)) or self.isMatch(s, p[2:])

        return first_character and s[1:] == p[1:] 


if __name__ == "__main__":
    obj = Solution()

    print(obj.isMatch(s = "aab", p = "c*a*b"))