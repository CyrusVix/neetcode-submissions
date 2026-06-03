class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix suffix method
        value = [1] * len(nums)

        prefix = 1 # neutral number does not break stuff
        for i in range(len(nums)):
            value[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in reversed(range(len(nums))):
            value[i] *= suffix
            suffix *= nums[i]
        return value
            
            