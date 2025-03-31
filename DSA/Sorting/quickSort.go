package sorting

func QuickSort(arr []int) {
    quickSortHelper(arr, 0, len(arr) - 1)
}

func quickSortHelper(arr []int, start, end int) {
    if start >= end || start < 0 || end < 0 {
        return
    }

    pivotIdx := partitionArray(arr, start, end)

    quickSortHelper(arr, start, pivotIdx - 1)
    quickSortHelper(arr, pivotIdx + 1, end)
}

func partitionArray(arr []int, start, end int) int {
    pivotIdx := end

    left, right := start, end - 1

    for left <= right {
        if arr[left] > arr[pivotIdx] && arr[right] < arr[pivotIdx] {
            arr[left], arr[right] = arr[right], arr[left]
        }

        for left <= end - 1 && arr[left] < arr[pivotIdx] {
            left++
        }

        for right >= 0 && arr[right] >= arr[pivotIdx] {
            right--
        }
    }

    arr[left], arr[pivotIdx] = arr[pivotIdx], arr[left]

    return left
}
