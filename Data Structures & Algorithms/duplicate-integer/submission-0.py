class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
       # if len(set(nums)) != len(nums):
       #     return True                  Inital attempt
       # return False
        

    
        