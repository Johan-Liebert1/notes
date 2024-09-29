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

## Single number in an array 

#### Given an array, every number appears atlest twice except one. Find that one

Trivial with a hash map, but we can use `XOR` operator for this.

If the array is [2, 2, 4, 1, 1]

then, the following solution works

```go
func singleNumber(nums []int) int {
    thingy := 0

    for _, n := range nums {
        thingy = thingy ^ n
    }

    return thingy
}
```

Here's how

```
thingy = 000

1. thingy = thingy ^ 2 = 000 ^ 010 = 010
2. thingy = 010 ^ 010 = 000
3. thingy = 000 ^ 100 = 100
4. thingy = 100 ^ 001 = 101
5. thingy = 101 ^ 001 = 100
```



