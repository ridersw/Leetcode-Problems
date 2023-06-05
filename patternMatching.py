class Solution:
    def problem(self, s1, s2):
        # words = []
        # word = ""
        # for swi in range(len(s2)):
        #     # print(f'Checking for word: {word} and char: {s2[swi]} and Final Word: {word + s2[swi]} and word + s2[swi] in s2: {word + s2[swi] in s2}')
        #     if word + s2[swi] in s2[swi+1:]:
        #         word += s2[swi]
        #     else:
        #         words.append(word)
        #         break

        # # removing the first words from the string
        # while words[0] in s2:
        #     index = s2.find(words[0])
        #     s2 = s2[:index] + s2[index+len(words[0]):]
        
        # print(f's2: {s2}')

        # y_count = s1.count('y')
        # y_length = len(s2) // y_count
        # words.append(s2[:y_length])

        # return words

        words = []

        firstPattern = "" + s1[0]

        for swi in range(len(s1)):
            if s1[swi] == firstPattern[-1]:
                firstPattern += s1[swi]

        


if __name__ == "__main__":
    obj = Solution()
    s1 = "xxxxyyxy"
    s2 = "gogogogopowerrangerpowerrangergopowerranger "
    print(obj.problem(s1, s2))


#input-  S1 = xxyyxy
# S2 :- gogopowerrangerpowerrangergopowerranger

#output- array = ['go', "powerranger"]