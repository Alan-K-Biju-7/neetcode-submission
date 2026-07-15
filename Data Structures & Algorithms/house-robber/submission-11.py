class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = []    
        for i in  range(len(nums)):
            dp.append(0)

        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])
        i = 2
        while i <= len(nums)-1:
            dp[i] = max(dp[i-2] + nums[i],dp[i-1])
            i +=1
          
        return dp[len(nums)-1]   