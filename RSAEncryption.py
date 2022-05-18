class Solution:
    def RSAEncryption(self, p, q, e, m):
        n = p * q
        print(f'n = p * q')
        print(f'n = {p} * {q}')
        print(f'n = {n}')
        print(f'ϕ(n) = (p-1) * (q-1)')
        print(f'ϕ(n) = {(p-1)} * {(q-1)}')


if __name__ == "__main__":
    obj = Solution()
    print(obj.RSAEncryption(p=3, q=11, e=7, m=5))