class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        connectionDict = {}
        for i in range(n):
            connectionDict[i] = []

        for elem in edges:
            connectionDict[elem[0]].append(elem[1])
            connectionDict[elem[1]].append(elem[0])


        
        visited = set()

        def dfs(nodeID,parentID):
            nonlocal visited

            if nodeID in visited:
                return True
            
            #never remove, as we want to detect cycles
            visited.add(nodeID)

            for adjacentNode in connectionDict[nodeID]:
                if adjacentNode != parentID:
                    if dfs(adjacentNode,nodeID):
                        return True

        
        return False if dfs(0,-1) else len(visited) == n