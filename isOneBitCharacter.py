class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        flag = False
        index = 0
        while index < len(bits):

            if index == len(bits) - 1:
                return True

            if bits[index] == 1:
                index += 2
            else:
                index += 1

        return flag

# We have two special characters:

# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

# Example 1:

# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:

# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.