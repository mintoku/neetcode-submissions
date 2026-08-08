class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep a map that stores the last index of each char
        mp = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if s[right] in mp:
                left = max(left, mp[s[right]] + 1)
            mp[s[right]] = right
            longest = max(longest, right - left + 1)
        
        return longest