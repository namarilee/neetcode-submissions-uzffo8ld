class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # maps course to prereqs
        pre_map = { i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        
        courses_taken = set()

        def dfs(course):
            if course in courses_taken: #already taken/visited
                return False
            if pre_map[course] == []: #has no prerequisites
                return True
            
            courses_taken.add(course)

            for pre in pre_map[course]:
                if not dfs(pre): #if we find one course that can't be completed
                    return False
                
            courses_taken.remove(course)
            pre_map[course] = []
            return True # can be taken
            
        # loop for every course in case of disconnected graph
        for course in range(numCourses):
            if not dfs(course): # return false once dfs returns false
                return False
        return True
