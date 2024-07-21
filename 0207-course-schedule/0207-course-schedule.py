class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = defaultdict(list)
        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)
        visited = [0] * numCourses
        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for prereq in adjacency_list[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 1
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True