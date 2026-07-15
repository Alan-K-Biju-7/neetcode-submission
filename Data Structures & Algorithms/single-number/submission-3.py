class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        
        for i in range(len(nums)):
            count = 0
            if nums[i] not in d:
                count = 1
                d[nums[i]] = count
            else:
                d[nums[i]] = d[nums[i]] + 1

        for k,v in d.items():
            if v == 1:
                return k       



        