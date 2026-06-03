class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #basis if s and t are equal length move foward
        if len(s) != len(t):
            return False

        d = {} #initiat dictionary
        for char in s:
            if char in d:
                d[char] += 1
            else: 
                d[char] = 1

        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False

        for val in d.values():
            if val != 0:
                return False
        
        return True