class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        prev_map = {}
        
        for n in nums:
            if n in prev_map:
                prev_map[n] += 1
            else: 
                prev_map[n] = 1
        return sorted(prev_map, key = lambda x: prev_map[x], reverse=True)[:k]
     