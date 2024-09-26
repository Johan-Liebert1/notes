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

## Lowest common binary tree ancestor

root, node1, node2

#### Approach 1

We can first check if `node1` is to the left of `root` or to the right
We can again check the same for `node2`

if `node1` is on the left and `node2` on right, then `root` is the LCA

if `node1` and `node2` both are on the left, the we can ignore the entire right tree and then make `root.Left` as the new node and recursively try


#### Approach 2

We can calculate the path to node1 and node2 from the root
Then we can iterate both path arrays at once, and whereever they diverge, the element to the left of that will be their LCA

If they don't diverge then one of them is the LCA, which we can find by checking the smaller path

          3
       /     \
      5       1
     /  \    /   \
    6    2  0     8
        /   \
       7     4
                    

#### if we want the LCA of 6 and 2

the paths will be `[3, 5, 6]` and `[3, 5, 2]`

They diverge after `5`, so `5` is LCA


#### if we want the LCA of 5 and 7

the paths will be `[3, 5]` and `[3, 5, 2, 7]`

They don't diverge, so the last element of the smaller path is the LCA
