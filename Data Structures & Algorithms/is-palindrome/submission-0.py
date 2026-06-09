class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        return cleaned == cleaned[::-1]




    #current thought process
        #1 use lowercase method from python (for cleaning) also remove spaces (figure out how)
        #2 reverse dictionary and store in dictionary list t
        #3 If s and t eual true return true, otherwise return false... dont think i need to check each positon since they should be equal value
            #
    
        
        