import heapq
from typing import List

"""  
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
"""


class Solution:
    def find_min_ratio(self, classes):
        idx = -1
        max_percentage_increase = 0

        # we want to check adding the student to which class will lead to the
        # maximum percentage increase

        for i, (p, s) in enumerate(classes):
            original = p / s

            if original == 1:
                continue

            percentage_increase = ((p + 1) / (s + 1)) - original

            if percentage_increase > max_percentage_increase:
                max_percentage_increase = percentage_increase
                idx = i

        return idx

    def maxAverageRatioWithoutHeap(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        while extraStudents > 0:
            # use heap
            min_idx = self.find_min_ratio(classes)

            # for passing, students in classes:

            classes[min_idx][0] += 1
            classes[min_idx][1] += 1

            extraStudents -= 1

        total_ratio = 0

        for passing, students in classes:
            total_ratio += passing / students

        return total_ratio / len(classes)

    # Better
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        my_heap = []

        for p, s in classes:
            # pushing (p / s) - (p + 1)/(s + 1) as it will always be negative and we'll get a max heap
            heapq.heappush(my_heap, (((p / s) - (p + 1) / (s + 1)), p, s))

        while extraStudents > 0:
            _, p, s = heapq.heappop(my_heap)

            p += 1
            s += 1

            extraStudents -= 1

            heapq.heappush(my_heap, (p / s - (p + 1) / (s + 1), p, s))

        return sum([p / s for _, p, s in my_heap]) / len(classes)
