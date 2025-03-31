from typing import List
import heapq


class Solution:

    def furthestBuilding(self, heights, bricks, ladders):
        heap = []

        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]

            if d > 0:
                # the next building is taller than the current one
                heapq.heappush(heap, d)

            if len(heap) > ladders:
                # we have more jumps required than we have ladders with us
                # so we use bricks
                # we also use the bricks to climb the shortest height as ladders are more powerful than bricks and can climb any height
                # so we need to save our ladders for larger heights and use our bricks for smaller heights
                bricks -= heapq.heappop(heap)

            if bricks < 0:
                # we used up bricks in the previous if and ended up with negative bricks
                # since we would only have entered the previous 'if' if we had less ladders than number of heights to climb
                # and we ran out of bricks while trying to climb the shortest distance, we return the index here as we cannot climb any more
                # we can still return 'i' here
                return i

        return len(heights) - 1

    # Dynamic Programming Solution (Extremely slow)
    def furthestBuildingDP(self, heights: List[int], bricks: int,
                           ladders: int) -> int:
        self.furthest = 0

        cache = {}

        def recurse(index, b, l):
            if (index, b, l) in cache:
                return

            if index == len(heights) - 1:
                self.furthest = index
                cache[(index, b, l)] = self.furthest
                return

            bricks_needed = heights[index + 1] - heights[index]

            # print(index, l, b, bricks_needed)

            if heights[index] < heights[index + 1]:
                if l <= 0 and b < bricks_needed:
                    self.furthest = max(index, self.furthest)
                    cache[(index, b, l)] = self.furthest
                    return

            if bricks_needed <= 0:
                recurse(index + 1, b, l)
            else:
                # current building is shorter than the next one, so we
                # can use either ladder or bricks
                if l >= 1:
                    recurse(index + 1, b, l - 1)

                if b >= bricks_needed:
                    recurse(index + 1, b - bricks_needed, l)

        recurse(0, bricks, ladders)

        return self.furthest
