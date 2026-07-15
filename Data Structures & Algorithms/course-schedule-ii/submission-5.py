class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visiting = set()
        visited = []
        for course, pre in prerequisites:
            graph[pre].append(course)

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            visiting.remove(course)
            visited.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        visited.reverse()    
        return visited            
                                 
        