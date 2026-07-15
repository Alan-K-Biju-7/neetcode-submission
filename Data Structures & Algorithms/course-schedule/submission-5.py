class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visiting = set()
        visited = set()
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
            visited.add(course)

            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True          


      