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

## k-th Largest element in an array

To find the k-th largest element in an array we have 3 options

#### Sort the array O(n * log n)
Sort the array, then get array[len - k]

#### Max Heap O(n + log n)
Put all elements in a max heap, then take out k elements

#### Quick Select. Worst case O(n^2). Avg Case O(n)

Similar to quicksort

1. Select a pivot
2. Partition the array, all elements lower than pivot to the left, and all greater to the right
3. Now whereever our pivot is, is out p-th largest element. 
We can check if the k-th largest will be to the left or right, and then run 1 and 2 on that partition of the array


In the worst case we might always choose the largest element as the pivot and k could be 1
Then we'll only reduce the array len by `len - 1`

## Majority element in an array

#### Majority element = element that occurs more than floor( len(array) / 2 ) times

1. We can use a hash map
2. or we can sort the array OR

#### Moore's voting algo
We will have a variable called count, and a var called element. `element, count := -1, 0` initially

We will just assume that the first element is our Majority element. 

We will have these cases

```go
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
```


the intuition is that, any number that appears more than n/2 times, will have a count of > 1 at the end

in the array `[ 7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5 ]`

we will start by assuming `7` is the majority element, and `count++` if the next element is 7, else `count--`

What happens is, for a particular subarray, if the count of `7` is equal to the count of `rest of the numbers`, count will be 0, else count will be > 0
So Whenever `count == 0` we reset the subarray kinda

## Every Subarray


```go
// we'll start from 0, 1, 2, 3, ...
for i := 0; i < len(array); i++ {
    // we want to end at 0, 1, 2, 3, ...
    for j := i; j < len(array); j++ {

        subarray := []int{}

        // this is where we get the actual subarray
        for k := i; k <= j; k++ {
            subarray = append(subarray, array[k])
        }
    }
}
```

## Maximum sum subarray

### Kadane's Algorithm

Example `[-2, -3, 4, -1, -2, 1, 5, -3]`

1. Initialize a varaible `sum := 0` and `maxSum := 0`. Sum will be our current sum
2. Loop through the array and add the element to `sum` then update `maxSum` accordingly
If `sum` ever goes below `0`, we simply reset it to `0` because there is no point in actually continuing with our current sum if it is negative
It's only going to lower our current sum, so we will reset it to `0` whenever it dips below `0`

```go
func maxSubArray(nums []int) int {
    sum := 0
    maxSum := -((1<<31) - 1)

    for _, n := range nums {
        sum += n

        maxSum = max(maxSum, sum)

        // Reset sum to 0, if it ever dips below zero
        sum = max(sum, 0)
    }

    return maxSum
}
```
