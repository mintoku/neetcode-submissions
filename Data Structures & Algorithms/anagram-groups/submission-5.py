class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a hashmap where 
        # - key is array of 26, each index represents a letter
        # - value is the count of strs that correspond
        wordsDict = defaultdict(list)

        for word in strs:
            charArray = [0] * 26
            for char in word:
                charArray[ord(char) - ord('a')] += 1
            wordsDict[tuple(charArray)].append(word)

        return list(wordsDict.values())