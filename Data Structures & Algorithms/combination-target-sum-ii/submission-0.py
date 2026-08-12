class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def backtrack(i, combo, total):
            if total == target:
                output.append(combo.copy())
                return

            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                if total + candidates[idx] > target:
                    break

                combo.append(candidates[idx])
                backtrack(idx + 1, combo, total + candidates[idx])
                combo.pop()

        backtrack(0, [], 0)
        return output