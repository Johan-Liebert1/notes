package sorting

import "fmt"

func MergeSort(array []int) {
    mergeSortHelper(array, 0, len(array) - 1)
}

// def merge_sorted_parts(arr, mid, end):
//     i, j = 0, mid + 1
//     
//     while i <= mid and j <= end:
//         if arr[i] <= arr[j]:
//             i += 1
//         else:
//             # Swap the element from the second part into the first part
//             arr[i], arr[j] = arr[j], arr[i]
//             i += 1
//             
//             # Ensure the second part remains sorted
//             temp = arr[j]
//             k = j
//             while k + 1 <= end and arr[k + 1] < temp:
//                 arr[k] = arr[k + 1]
//                 k += 1
//             arr[k] = temp

func mergeExtraSpace(array []int, start1, end1, start2, end2 int) {
}

func mergeSortHelper(array []int, start, end int) {
    if start == end {
        return
    }

    if end - start == 1 {
        if array[end] < array[start] {
            array[end], array[start] = array[start], array[end]
        }

        return
    }

    mid := start + (end - start) / 2

    mergeSortHelper(array, start, mid)
    fmt.Printf("array[%d:%d]: %+v\n", start, mid, array[start:mid])

    mergeSortHelper(array, mid + 1, end)
    fmt.Printf("array[%d:%d]: %+v\n", mid + 1, end, array[mid + 1:end])
}
