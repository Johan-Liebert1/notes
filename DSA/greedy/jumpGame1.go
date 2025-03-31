package greedy

func canJump(nums []int) bool {
	if len(nums) == 1 {
		return true
	}

	currentJumpIndex := 0

	for {
		// let's be greedy and jump the furthest
		furthestJump := nums[currentJumpIndex] + currentJumpIndex

		if furthestJump >= len(nums)-1 {
			return true
		}

		bestNextJump := currentJumpIndex

		for i := currentJumpIndex + 1; i <= furthestJump; i++ {
			if i+nums[i] > bestNextJump+nums[bestNextJump] {
				bestNextJump = i
			}
		}

		if currentJumpIndex == bestNextJump {
			return false
		}

		currentJumpIndex = bestNextJump
	}
}

// Our first goal is len(nums) - 1
// we will iterate the array in reverse and check if at any index we can reach the end
// if we can, we make the new index our goal as if we can reach the new index, then we can 
// definitely reach the end
func canJumpFaster(nums []int) bool {
    goal := len(nums) - 1

    for i := len(nums) - 1; i >= 0; i-- {
        if i + nums[i] >= goal {
            goal = i
        }
    }

    return goal == 0
}
