from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        all_configs = []

        for [w, l, h] in cuboids:
            all_configs.append([w, l, h])
            all_configs.append([h, l, w])
            all_configs.append([w, h, l])

        all_configs.sort(key=lambda x: x[0] * x[1])

        print(all_configs)

        # find LIS of all_configs

        cuboids = [a[2] for a in all_configs]
        sequence = [None] * len(all_configs)
        max_idx = 0

        for i in range(len(all_configs)):
            iw, il, ih = all_configs[i]

            for j in range(i):
                jw, jl, jh = all_configs[j]

                if jw <= iw and jh <= ih and jl <= il:
                    if cuboids[i] + cuboids[j] >= cuboids[i]:
                        cuboids[i] += cuboids[j]
                        sequence[i] = j

            if cuboids[i] >= cuboids[max_idx]:
                max_idx = i

        print(cuboids, sequence)

        height = 0

        while max_idx is not None:
            print(f"{max_idx = }")
            height += all_configs[max_idx][2]
            max_idx = sequence[max_idx]

        return height


print(Solution().maxHeight([[50, 45, 20], [95, 37, 53], [45, 23, 12]]))
