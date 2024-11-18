## Prefix and Suffix Sums

Whenever working with prefix sum and suffix sum both, we can simply sum the entire array and then 
while calculating the prefix/suffix sum, keep subtracting the current number to get the suffix/prefix 
sum respectively.

```go
func pivotIndex(nums []int) int {
	sum := 0

    // Sum up the array
	for _, v := range nums {
		sum += v
	}

	left := 0

	right := sum

	for i, v := range nums {
        // subtract the current number to get suffix sum
		right -= v

		if left == right {
			return i
		}

		left += v

	}

	return -1
}
```

## Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

![RainWater Trap](./rainwatertrap.png)

### Approach 1

We can have a suffix sum array, and keep track of the left max while traversing the array.
Since there need to be walls on left and right for water to be stored, the formula is `water += min(leftMax, rightMax) - height[i]`

Take, idx 5 for example, `leftMax = 2`, `rightMax = 3` and `height = 1`, so water it holds = `water = min(2, 3) - 1 = 2 - 1 = 1`

```go
func trap(height []int) int {
    tallestUntilIndex := make([]int, len(height))
    tallestUntilIndex[len(height) - 1] = height[len(height) - 1]

    for i := len(height) - 2; i >= 0; i-- {
        tallestUntilIndex[i] = max(tallestUntilIndex[i + 1], height[i])
    }

    water := 0
    leftMax := 0

    for i := 0; i < len(height); i++ {
        leftMax = max(leftMax, height[i])

        minn := min(leftMax, tallestUntilIndex[i])

        if minn > height[i] {
            water += (minn - height[i])
        }
    }

    return water
}
```

### Approach 2

We'll take a two pointer approach. We'll have a left and a right pointer initially at `0` and `len(height) - 1`
Also, `leftMax = 0, rightMax = 0` initially
