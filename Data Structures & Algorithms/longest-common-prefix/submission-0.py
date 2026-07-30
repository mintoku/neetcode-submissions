class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        right = len(prefix)
        for word in strs:
            if right > len(word):
                right = len(word)
            while word[:right] != prefix[:right] and right > 0:
                right -=1
        return prefix[:right]