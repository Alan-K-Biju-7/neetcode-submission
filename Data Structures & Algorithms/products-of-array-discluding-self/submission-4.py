class Solution:
   
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n # [1,1,1,1]

        prefix = 1    
        for i in range(n): # i = 3
            res[i] = prefix # [1,1,2,8]

            prefix *= nums[i] #  prefix = 8

        postfix = 1 # postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix # [1,1,1,1]
            postfix *= nums[i] # postfix = 1

        return res
                   

        