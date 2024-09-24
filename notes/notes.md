## Greatest Common Divisor

```py
def gcd_recursive(a, b):
    if a == 0 or b == 0:
        return max(a, b)

    else:
        return gcd_recursive(b, a % b)


def gcd_iterative(a, b):
    if a == 0 or b == 0:
        return max(a, b)

    # This is basically dividing a by b, or b by a depending upon which one's larger
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return b

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
