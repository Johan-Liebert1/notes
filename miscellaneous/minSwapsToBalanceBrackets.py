class Solution:
    def minSwaps(self, s: str) -> int:
        extra_closing = 0
        max_extra_closing = 0

        # if we get a closing bracket before an opening bracket then that's bad as there was nothing to close
        # so the min number of swaps will be the max number of useless closing brackets ever

        for i in s:
            if i == "[":
                extra_closing -= 1
            else:
                extra_closing += 1
                max_extra_closing = max(max_extra_closing, extra_closing)

        # divide the max_extra_closing by 2 as every swap decrements the number of max_extra_closing by 2
        # add 1 at the end as we get the ceil value
        return (max_extra_closing + 1) // 2
