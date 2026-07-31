class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # variable prefix; first set it to the first word in the list
        # then interate through the rest of the list
        # iterate from first letter -> last letter of shortest word or until the letters differ
        # that will be prefix
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(strs[i]), len(prefix)):
                if strs[i][j] != prefix[j]:
                    break
                j+=1
            prefix = prefix[:j]
        return prefix