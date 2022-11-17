class Solution:
    def findWords(self, board, words):
        temp = {}
        for word in words:
            temp[word[0]] = []
            for swi in range(len(board[0])):
                if word[0] in board[swi]:
                    index_ref = board[swi].index(word[0])
                    temp[word[0]].append([swi, index_ref])

        return temp




if __name__ == "__main__":
    obj = Solution()

    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    print(obj.findWords(board, words))