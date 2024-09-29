package arrays

// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
// You must implement a solution with a linear runtime complexity and use only constant extra space.

func singleNumber(nums []int) int {
    thingy := 0

    for _, n := range nums {
        thingy = thingy ^ n
    }

    return thingy
}
