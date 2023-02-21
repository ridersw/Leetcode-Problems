def count_words(wordLen, maxVowels):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    def generate_words(word, num_vowels):
        if len(word) == wordLen:
            return 1
        count = 0
        for letter in vowels:
            if num_vowels < maxVowels:
                count += generate_words(word + letter, num_vowels + 1)
            else:
                count += generate_words(word + letter, num_vowels)
        for letter in consonants:
            count += generate_words(word + letter, 0)
        return count
    
    return generate_words("", 0)

print(count_words(5, 2))