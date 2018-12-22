"""
Given any two words, check if a word is an anagram of another.
For Example : God – dog, strip – trips, iced – dice, lion – loin ;)
"""


def check_anagram(word_1, word_2):
    word_1 = sorted(set(word_1))
    word_2 = sorted(set(word_2))

    if word_1 == word_2:
        return True
    else:
        return False


word1 = input('Enter the first word : ')
word2 = input('Enter the second word : ')
print(check_anagram(word1, word2))
