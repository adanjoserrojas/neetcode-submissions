class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Based Case
        # Combinations
        # Constraints
        # Backtrack

        wanted = 0
        res = []

        def dfs(index, path, wanted):

            if wanted == target:
                res.append(path.copy())
                return
            if index >= len(nums) or wanted > target:
                return

            # Decision 1 if the wanted < target add a num
            path.append(nums[index])
            dfs(index, path, wanted + nums[index])
            path.pop()

            dfs(index + 1, path, wanted)                

        dfs(0, [], wanted)

        return res
        