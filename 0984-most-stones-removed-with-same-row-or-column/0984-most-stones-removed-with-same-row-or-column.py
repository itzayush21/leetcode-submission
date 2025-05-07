class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        graph = defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if i != j and (x1 == x2 or y1 == y2):
                    graph[i].append(j)

        visited = set()

        def dfs(i):
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)

        components = 0
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                components += 1

        
        return len(stones) - components
        