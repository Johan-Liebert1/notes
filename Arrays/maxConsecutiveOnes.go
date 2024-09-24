package main

// Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
// 
// Example 1:
// 
// Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
// Output: 6
// Explanation: [1,1,1,0,0,1,1,1,1,1,1]
// Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
// Example 2:
// 
// Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
// Output: 10
// Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
// Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

func longestOnes(nums []int, k int) int {
    left := 0
    right := 0

    currentOnes := 0
    maxOnes := 0

    for right < len(nums) {
        if nums[right] == 1 {
            currentOnes += 1
            right++
        } else if k > 0 {
            k--
            currentOnes += 1
            right++
        } else if k == 0 {
            if nums[left] == 0 {
                k++
            }

            currentOnes--
            left++
        }

        if currentOnes > maxOnes {
            maxOnes = currentOnes
        }

    }

    return maxOnes
}
