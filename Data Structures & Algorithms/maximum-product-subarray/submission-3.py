class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                temp = maxi
                maxi = mini
                mini = temp
            maxi = max(nums[i],nums[i] * maxi)    
            mini = min(nums[i],nums[i] * mini)
            ans = max(ans,maxi)
        return ans    
