class Solution:
    def jump(self, flagHeight, bigJump):
        return ((flagHeight // bigJump) + (flagHeight % bigJump))

if __name__ == "__main__":
    flagHeight = 8
    bigJump = 3

    obj = Solution()
    print(obj.jump(flagHeight, bigJump))