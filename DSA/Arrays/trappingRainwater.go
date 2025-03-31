package arrays

func trap(height []int) int {
    tallestUntilIndex := make([]int, len(height))
    tallestUntilIndex[len(height) - 1] = height[len(height) - 1]

    for i := len(height) - 2; i >= 0; i-- {
        tallestUntilIndex[i] = max(tallestUntilIndex[i + 1], height[i])
    }

    water := 0
    leftMax := 0

    // now we are the first block that has a height of > 0
    for i := 0; i < len(height); i++ {
        leftMax = max(leftMax, height[i])

        minn := min(leftMax, tallestUntilIndex[i])

        if minn > height[i] {
            water += (minn - height[i])
        }
    }

    return water
}
