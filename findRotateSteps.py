class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.turns = float("inf")
        self.key = key
        self.rotateDial(ring, 0, 0)
        print(f'turns: {self.turns}')
        
        return self.turns
        
    def rotateDial(self, ring, keyCharIndex, turn):

        if keyCharIndex >= len(self.key):
            self.turns = min(self.turns, turn)
            return
        
        # print(f'keyCharIndex: {keyCharIndex} and key: {self.key}')
        # print(f'Current Key: {self.key[keyCharIndex]} and Current Ring: {ring} and Current Turns: {turn}')

        if self.key[keyCharIndex] == ring[0]:
            # print(f'Found Key: {self.key[keyCharIndex]} at Ring: {ring} with total turns: {turn + 1}')
            self.rotateDial(ring, keyCharIndex+1, turn+ 1) 
        
        # rotate anticlockwise
        
        for index in range(len(ring)):
            if ring[index] == self.key[keyCharIndex]:
                newRing = ring[index:] + ring[:index]
                # print(f'Rotated Anticlockwise Found Key: {self.key[keyCharIndex]} at Ring: {newRing} with total turns: {turn + index + 1}')
                if (turn + index + 1) > self.turns:
                    return
                self.rotateDial(newRing, keyCharIndex+1, turn+ index + 1) 

        
            
        tempRing = ring[:0+1] + ring[1:][::-1]
        # print(f'tempRing: {tempRing}')
        # rotate clockwise
        for index in range(len(tempRing)):
            if tempRing[index] == self.key[keyCharIndex]:
                newRing = tempRing[index:] + tempRing[:index]
                if (turn + index + 1) > self.turns:
                    return
                # print(f'Rotated Clockwise Found Key: {self.key[keyCharIndex]} at Ring: {newRing} with index: {index} and total turns: {turn + index + 1}' )
                self.rotateDial(newRing, keyCharIndex+1, turn+ index + 1) 
            
if __name__ == "__main__":
    obj = Solution()
    print(obj.findRotateSteps("abcde", "ade"))

# In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

# Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

# Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

# At the stage of rotating the ring to spell the key character key[i]:

# You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
# If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
 

# Example 1:


# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
# For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.
# Example 2:

# Input: ring = "godding", key = "godding"
# Output: 13
 

# Constraints:

# 1 <= ring.length, key.length <= 100
# ring and key consist of only lower case English letters.
# It is guaranteed that key could always be spelled by rotating ring.