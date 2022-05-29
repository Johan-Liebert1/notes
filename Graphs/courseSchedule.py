from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for prereq, course in prerequisites:
            if prereq == course:
                return False

            d[prereq].append(course)

            if course not in d:
                d[course] = []

        visited = {n: -1 for n in d}

        if len(d.keys()) == 0:
            return True

        queue = [prerequisites[0][0]]

        print(d, visited)

        """
        -1 -> node is unvisited
         1 -> Node is processed
         2 -> Node is being processed
        """

        for vertex in d:
            print(queue)

            node = vertex if len(queue) == 0 else queue[0]

            if visited[node] == 1:
                queue = queue[1:]
                continue

            # processing the current node
            visited[node] = 2

            for prereq in d[node]:
                if visited[prereq] != -1:
                    # reached a node while it's being processed, i.e. found a loop
                    return False

                queue.append(prereq)

            visited[node] = 1
            if len(queue) > 0:
                queue = queue[1:]

        return True


print(Solution().canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
