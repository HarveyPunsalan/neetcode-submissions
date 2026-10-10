class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = {}

        for word in strs:
            word_key = tuple(sorted(word))

            if word_key not in grouped_words:
                grouped_words[word_key] = []

            grouped_words[word_key].append(word)

        return list(grouped_words.values())
        