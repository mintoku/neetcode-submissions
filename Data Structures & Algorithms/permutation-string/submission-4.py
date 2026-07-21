class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)
        counted1 = Counter(s1)
        counted2 = Counter(s2[left:right])
        while right < len(s2):
            if counted1 == counted2: return True
            counted2[s2[left]] -= 1
            counted2[s2[right]] += 1
            left += 1
            right += 1
        return counted1 == counted2