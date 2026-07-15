class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        max_sum = nums[0]
        
        dp[0] = nums[0]


        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1] + nums[i])
            max_sum = max(max_sum,dp[i])
        return max_sum    
        