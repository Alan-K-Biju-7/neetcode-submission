class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(index,path,total):
            if target == total:
                result.append(path.copy())
                return 
            if target < total or index == len(nums):
                return

            path.append(nums[index])
            dfs(index,path,total + nums[index])

            path.pop()
            dfs(index+1,path,total)

        dfs(0,[],0)  
        return result   
