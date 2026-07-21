class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        freq = {}
        longest = 0
        maxFreq = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            windowLen = right - left + 1
            toReplace = windowLen - maxFreq
            if toReplace > k:
                freq[s[left]] -= 1
                left += 1
            else:
                longest = max(windowLen, longest)
            right += 1
        return longest

        