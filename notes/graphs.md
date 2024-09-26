## Delete from middle of linked list

### Easy way
Traverse linked list twice, once to find the length and once to delete the middle

### Have a slow pointer and a fast pointer. The fast pointer moves twice as fast as the slow one

So, when the fast ptr is at the end, the slow pointer will be directly in the middle


Example


```
LL -> 1, 2, 3, 4, 5

Iter 1
slow = 1, fast = 1

Iter 2
slow = 2, fast = 3

Iter 3
slow = 3, fast = 5
```

## Copying an array in go

```go
newArray := make([]Type, len(arrayToCopy))
copy(newArray, arrayToCopy)
```
