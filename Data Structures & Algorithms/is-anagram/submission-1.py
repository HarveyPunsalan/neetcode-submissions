class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_counts = {}

        for letter in s:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

        for letter in t:
            if letter not in letter_counts:
                return False

            letter_counts[letter] -= 1

        return all(number == 0 for number in letter_counts.values())
        