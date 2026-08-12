class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #every character is mapped to a set of their adj chars
        adj = { char: set() for word in words for char in word }

        #going through every single pair
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            #edge case: if prefix of both words are the same but word1 is longer than word2
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            #go through shorter word
            for j in range(min_len):
                #if letters are different
                if word1[j] != word2[j]:
                    #add character mapping
                    #char in word2 comes after char in word1
                    adj[word1[j]].add(word2[j])
                    break #only want first different char
        
        visited = {} #each character is assigned to True or False
        output = [] #will join and reverse at the end

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True

            visited[char] = False
            output.append(char)

        
        for char in adj:
            if dfs(char):
                return ""

        output.reverse()
        return "".join(output)

