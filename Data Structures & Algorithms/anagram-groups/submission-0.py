class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # key: charCount, value: list of anagrams

        for str in strs:
            count = [0] * 26 # has 26 zeroes for a...z

            for c in str:
                count[ord(c) - ord("a")] += 1 # subtracting a's ascii value from each character to get 0-26 
            
            result[tuple(count)].append(str)

        return result.values()
# time complexity: O(m*n*26) -> O(m*n) m = # of strings, n = avg length of string