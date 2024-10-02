package main

import (
	"coding-questions/Arrays"
	"fmt"
)

func main()  {
    nums := []int{0, 1, 0, 3, 12}
    arrays.MoveZeroes2(nums)

    fmt.Printf("nums: %+v\n", nums)
    
}
