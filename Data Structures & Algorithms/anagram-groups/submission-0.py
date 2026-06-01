
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        full_list = {}
        for word in strs: #goes through every value in the list and the postion of them
            key = "".join(sorted(word))
            if key in full_list:
                full_list[key].append(word)
            else: 
                full_list[key] = [word] 
        return list(full_list.values())

    


        
        
        