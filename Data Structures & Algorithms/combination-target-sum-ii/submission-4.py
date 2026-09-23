class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(index, path, total):

            if target == total:
                res.append(path[:])
                return

            if total > target or index == len(candidates):
                return
            
            path.append(candidates[index])
            dfs(index + 1, path, total + candidates[index])
            path.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, path, total)
        

        dfs(0, [], 0)
        return res