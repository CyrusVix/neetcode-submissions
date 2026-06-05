class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set: #found start
                count = 1
                while (n + count) in num_set:
                    count += 1
                longest = max(longest, count)
        return longest    
