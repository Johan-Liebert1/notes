package arrays

// Given a binary array nums, you should delete one element from it.
// 
// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
// 
// Example 1:
// 
// Input: nums = [1,1,0,1]
// Output: 3
// Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
// Example 2:
// 
// Input: nums = [0,1,1,1,0,1,1,0,1]
// Output: 5
// Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
// Example 3:
// 
// Input: nums = [1,1,1]
// Output: 2
// Explanation: You must delete one element.

func longestSubarray(nums []int) int {
    subarrayStart := 0

    for _, n := range nums {
        if n == 1 {
            break
        }

        subarrayStart++
    }

    if subarrayStart >= len(nums) {
        // entire array is filled with zeroes
        return 0
    }

    // now subarrayStart points to the first '1' in the array

    lastRemovedElement := -1
    longestSubarrayLen := 1

    i := subarrayStart + 1

    for i < len(nums) {
        if nums[i] == 0 {
            // We haven't removed any element, so no we can 
            if lastRemovedElement == -1 {
                // remove this element and keep track of it
                lastRemovedElement = i
                
                i++
            } else {
                // longestSubarrayLen = max(longestSubarrayLen, i - subarrayStart)

                subarrayStart = lastRemovedElement

                for subarrayStart < len(nums) && nums[subarrayStart] == 0 {
                    subarrayStart++
                }

                if subarrayStart >= len(nums) {
                    break
                }

                i = subarrayStart + 1
                lastRemovedElement = -1
            }

            continue
        }

        if lastRemovedElement == -1 {
            longestSubarrayLen = max(longestSubarrayLen, i - subarrayStart + 1)
        } else {
            longestSubarrayLen = max(longestSubarrayLen, i - subarrayStart)
        }

        i++
    }

    // Entire array is 1s and we must delete one element
    if longestSubarrayLen == len(nums) {
        return len(nums) - 1
    }

    return longestSubarrayLen
}
