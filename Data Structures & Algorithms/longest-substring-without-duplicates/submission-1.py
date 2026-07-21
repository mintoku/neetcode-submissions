class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        left, right = 0,0
        length = 0
        while right < len(s):
            while s[right] in s[left:right] and left < right:
                left+= 1
            length = max(length, right-left)
            right += 1
        return length + 1