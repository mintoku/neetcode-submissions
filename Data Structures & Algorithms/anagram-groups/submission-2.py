class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = {}
        for word in strs:
            character_array = [0] * 26
            for char in word:
                character_array[ord(char) - ord('a')] += 1
            # we need a key but lists cannot be keys so we made count a tuple
            key = tuple(character_array)
            if key in words_dict:
                words_dict[key].append(word)
            else:
                words_dict[key] = [word]
        return list(words_dict.values())