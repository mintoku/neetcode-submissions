class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea create hashmap
        # key: sorted word
        # value: list of words in strs its an anagram of

        groups = defaultdict(list)

        for word in strs:
            groups["".join(sorted(word))].append(word)
        
        return list(groups.values())