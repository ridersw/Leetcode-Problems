from platformdirs import user_cache_dir


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        userPattern = {}

        for swi in range(len(username)):
            if username[swi] in userPattern:
                userPattern[username[swi]].append(website[swi])
            else:
                userPattern[username[swi]] = [website[swi]]

        print(f'userPattern: {userPattern}')

if __name__ == "__main__":
    obj = Solution()
    print(obj.mostVisitedPattern(username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]))