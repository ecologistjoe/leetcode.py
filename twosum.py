#leetcode problem #1.
# find indices of values in a list that sum to a target

class Solution:
    
    # The naive O^2 time approach
    def twoSumO2(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1, N):
                
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        return None #Should not happen
    
    
    
    # Use a dictionary (hash table) to invert value->index relationship
    # then use it to look up if the addend compliment exists, and if so, where
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        
        d = {}
        for i, v in enumerate(nums):
            addend = target-v
            if addend in d:
                return [d[addend], i]
            d[v] = i
        
        return None #fallback