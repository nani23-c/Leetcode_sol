class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False for i in range(n)]

        def dfs(u):
            visited[u]=True
            if u==destination:
                return
            for v in graph[u]:
                if v==destination:
                    visited[v]=True
                    return


                if not visited[v]:
                    dfs(v)
        dfs(source)

        return visited[destination]


        