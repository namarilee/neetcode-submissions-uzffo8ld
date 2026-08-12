class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        # a course has 3 possible states:

        #visited -> course has been added to output
        #visiting -> course not added to output, but added to cycle
        #unvisited -> course not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return output

