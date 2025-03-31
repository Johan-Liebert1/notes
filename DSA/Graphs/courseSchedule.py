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

        # Time limit exeeds if we only keep track of visited nodes as they will be processed again and again
        # on each iteration
        visited = {n: {"visited": False, "visiting": False} for n in d}

        if len(d.keys()) == 0:
            return True

        def cycle(node):
            if visited[node]["visited"]:
                return False

            if visited[node]["visiting"]:
                return True

            c = False

            visited[node]["visiting"] = True

            for neighbor in d[node]:
                if cycle(neighbor):
                    return True

            visited[node]["visiting"] = False
            visited[node]["visited"] = True

            return False

        ccycle = False

        for node in d:
            visited[node]["visiting"] = True

            for neighbor in d[node]:
                ccycle = cycle(neighbor)

                if ccycle:
                    return False

            visited[node]["visiting"] = False
            visited[node]["visited"] = True

        return True


print(Solution().canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
