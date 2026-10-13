class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        index = 0

        while index < len(s):
            separator_index = index

            while s[separator_index] != "#":
                separator_index += 1

            word_length = int(s[index:separator_index])

            word_start = separator_index + 1
            word_end = word_start + word_length

            word = s[word_start:word_end]
            decoded_strings.append(word)

            index = word_end

        return decoded_strings
