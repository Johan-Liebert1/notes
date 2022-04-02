# our goal is at the end at the beginning
# then we check if we can reach the goal using the previous value
# if we can then just shift the goal to the left as if we can reach the original goal
# with the previous value, then all we need is to reach the previous value so that can be the goal now
def canJump(nums: list[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0
