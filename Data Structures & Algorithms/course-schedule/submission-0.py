class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses) }

        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited: # cycle detected
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            preMap[course] = []
            return True
             
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True