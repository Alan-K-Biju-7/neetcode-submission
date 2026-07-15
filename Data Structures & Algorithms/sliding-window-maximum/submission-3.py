class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        res = []
        max_element = 0
        for i in range(len(nums)):
            max_element = max(nums[i:i+k])
            res.append(max_element)
            if i + k >= len(nums):
                break
        return res    
            

        