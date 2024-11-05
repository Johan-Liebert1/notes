package arrays

// Find majority element in an array 
// Majority element = element that occurs more than floor( len(array) / 2 ) times
func majorityElement(nums []int) int {
    element := -1
    count := 0

    for _, n := range nums {
        if count == 0 {
            count++
            element = n
        } else {
            if n == element {
                count++
            } else {
                count--
            }
        }
    }

    return element
}
