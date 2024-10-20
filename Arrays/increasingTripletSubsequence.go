package arrays


func increasingTriplet(nums []int) bool {
    // We will keep track of two variables, last and last_last
    first := 1<<31 - 1
    second := 1<<31 - 1

    for _, val := range nums {
        if val < first {
            first = val
        } else if val < second {
            second = val
        } else {
            return true
        }
    }

    return false
}
