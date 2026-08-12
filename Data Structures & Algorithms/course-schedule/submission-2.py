class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for pr in prerequisites:
            adj_list[pr[1]].append(pr[0])
        
        #if a cycle is detected, it is impossible
        # call courses along the curr dfs path
        visiting = set()

        def dfs(course):
            if course in visiting: #visit a course twice
                #cycle detected
                return False

            #has no prereqs
            if adj_list[course] == []:
                return True
            
            visiting.add(course)
            for pr in adj_list[course]:
                # if function returns false, return false for entire function
                if not dfs(pr):
                    return False 
            
            visiting.remove(course) #done visiting
            adj_list[course] = [] 
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True