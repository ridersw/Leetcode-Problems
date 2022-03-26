
class Solution:
    def kWeakestRows(self, mat, k):
        weakRanks = []

        for swi in range(len(mat)):
            weakRanks.append(mat[swi].count(1))

        print(f'weakRanks: {weakRanks}')

        res = []
        maxNumber = max(weakRanks)
        for swi in range(k):
            ind = weakRanks.index(min(weakRanks))
            res.append(ind)
            weakRanks[ind]= maxNumber + 1

        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.kWeakestRows(mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], k = 3))
    print(obj.kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2))