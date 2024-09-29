## Binary Search

```go
// range 1 to n
left, right := 1, n

for left <= right {
    // we could've gotten the midpoint by doing (left + right) / 2
    // But that could cause integer overflow

    mid := left + (right - left) / 2

    result := guess(mid)
    
    // our guess is correct
    if result == 0 {
        return mid
    } else if result == 1 {
        // our guess is lower so we disregard the left side
        left = mid + 1
    } else {
         // our guess is higher so we disregard the right side
        right = mid - 1
    }
}
```

## Binary Search to find element greater than or equal to

```go
// returns the index of where it found the element greater than or eq to toFind 
// if it doesn't find the element, returns -1
func search(toFind int) int {
    left, right := 0, len(potions) - 1
    
    result := -1 

    for right >= left {
        mid := left + (right - left) / 2

        if potions[mid] >= toFind {
            result = mid

            // continue searching in the left half
            // as the array could be [0, 5, 6, 6, 6, 6, 7]
            // and we are searching for 6
            right = mid - 1
        } else {
            // search in the right half
            left = mid + 1
        }
    }

    return result
}
```

## Pivot Index

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
