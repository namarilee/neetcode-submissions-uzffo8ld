class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def backtrack(i, combo, total):
            if total == target:
                output.append(combo.copy())
            
            for j in range(i, len(candidates)):
                #if the two numbers next to each other are the same, skip this iteration
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if total > target or i >= len(candidates):
                    break
                
                combo.append(candidates[j])
                backtrack(j + 1, combo, total + candidates[j])
                combo.pop()
        
        backtrack(0, [], 0)
        return output