from typing import List


class Solution:
    def minReorder(self, x: int, connections: List[List[int]]) -> int:
        visited = set()
        graph = { c: [] for c in range(x) }
        
        for from_, to in connections:
            graph[from_].append(to)
            graph[to].append(from_)
            
        can_reach = { (a, b) for a,b in connections }
        changes = 0
        
        '''
        start from 0
        check if all of 0's neighbors can reach it, if not then reverse the arrow
        now check if all of 0's neighbors' neighbors can reach 0's neighbors
        and so on
        '''
        def dfs(node):
            nonlocal changes
            
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                
                if (neighbor, node) not in can_reach:
                    # cannot reach node from n
                    # which is not good
                    changes += 1
                    
                visited.add(neighbor)
                
                dfs(neighbor)
        
        visited.add(0)
        dfs(0)
        
        return changes
                    
                    
