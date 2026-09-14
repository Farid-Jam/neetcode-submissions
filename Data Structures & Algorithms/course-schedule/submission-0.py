class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1
        
        queue = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
                
        return True if inDegree == [0] * numCourses else False