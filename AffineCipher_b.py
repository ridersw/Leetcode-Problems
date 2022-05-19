class Solution:
    def egcd(self, a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y

    def modinv(self,a, m):
        gcd, x, y = self.egcd(a, m)
        if gcd != 1:
            return None # modular inverse does not exist
        else:
            return x % m


    # affine cipher encryption function
    # returns the cipher text
    def affine_encrypt(self, text, key):
        '''
        C = (a*P + b) % 26
        '''
        return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                    + ord('A')) for t in text.upper().replace(' ', '') ])


    # affine cipher decryption function
    # returns original text
    def affine_decrypt(self, cipher, key):
        '''
        P = (a^-1 * (C - b)) % 26
        '''
        return ''.join([ chr((( self.modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                        % 26) + ord('A')) for c in cipher ])

    def calculateGCD(self, a, b):
        if b == 0:
            return a
        if a < b:
            return self.calculateGCD(b, a)
        return self.calculateGCD(b, a%b)
        
        


if __name__ == "__main__":
    obj = Solution()
    text = ""
    with open('input.txt') as f:
        text = f.readlines()

    text = text[0]
    print(f"Text Readed from the File: {text}")

    while True:
        a = input("Enter Key 1 (a): ")
        ans = obj.calculateGCD(int(a), 26)
        if ans == 1:
            break

    while True:
        b = input("Enter Key 2 (b): ")
        if int(b) > 0 and int(b) <26:
            break
    
    key = [int(a), int(b)]
    affine_encrypted_text = obj.affine_encrypt(text, key)
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
    print('Decrypted Text: {}'.format(obj.affine_decrypt(affine_encrypted_text, key) ))