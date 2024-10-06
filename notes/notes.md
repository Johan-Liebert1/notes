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

## Monotonic Stack

Whenever trying to find smaller or larger element to the right or left of an index in an array, we can use a monotonic stack.

Example, at every element in `[73, 74, 75, 71, 69, 72, 76, 73]` find the closest element to the right that's greater than it if it exists, else put -1

Answer should be `[(1, 74), (2, 75), (6, 76), (5, 72), (5, 72), (6, 76), -1, -1]`. In the form `(index, element)`

We can solve this by iterating from the right, and keeping each element in a stack until we find an element that's larger than the current 
element we're iterating over.

#### Add `73` to stack

```i = 7; el = 73; stack = [73]; output = -1```

#### Add `76` to stack

```i = 6; el = 76; stack = [73, 76]; output = -1```

#### Add `72` to stack and add `76` to the output array

```i = 5; el = 72; stack = [73, 76, 72]; output = 76```

#### Add `69` to stack and add `72` to the output array

```i = 4; el = 69; stack = [73, 76, 72, 69]; output = 72```

#### Remove `69` from stack as `69 <= 71` and add `71` to the output array

```i = 3; el = 71; stack = [73, 76, 72, 71]; output = 72```

#### Remove `69`, `72` from stack as `69 <= 71` and `72 <= 75` and add `76` to the output array

```i = 2; el = 75; stack = [73, 76, 75]; output = 76```

#### Add 74 to stack.

```i = 1; el = 74; stack = [73, 76, 75, 74]; output = 75```

#### Add 73 to stack.

```i = 0; el = 73; stack = [73, 76, 75, 74, 73]; output = 74```
