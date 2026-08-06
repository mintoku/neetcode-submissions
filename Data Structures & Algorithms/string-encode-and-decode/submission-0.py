class Solution:
    # idea: #5Hello#5World

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            nextLen = ""
            while s[i] != "#":
                nextLen += s[i]
                i+=1
            result.append(s[i+1:i+int(nextLen)+1])
            i += int(nextLen)+1
        return result

