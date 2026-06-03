class Solution:

    def encode(self, strs: List[str]) -> str:
        value = ""
        for i in strs:
            value += str(len(i)) + "#" + i
        return value

    def decode(self, s: str) -> List[str]:
        value = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            value.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return value