class Solution:
    def semordnilap(self, arr):
        result = []
        done = set()

        for word in arr:
            if word[::-1] in arr and word[::-1] not in done:
                result.append([word, word[::-1]])
                done.add(word)
                done.add(word[::-1])

        return result


if __name__ == "__main__":
    obj = Solution()

    words = ["diaper", "abc", "test","cba", "repaid"]

    print(obj.semordnilap(words))