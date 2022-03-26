from curses.ascii import SO


class Solution:
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

if __name__ == "__main__":
    obj = Solution()

    print(obj.removeDuplicateLetters(s = "bcabc"))