'''Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

Example

For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
kthLargestElement(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
kthLargestElement(nums, k) = 99.'''

#======================IMPLEMENT USING HEAPS==================

nums = [7, 6, 5, 4, 3, 2, 1]

def kthLargest(array, k):
    new_arr = sorted(array)

    return new_arr[len(new_arr) - k]


print(kthLargest(nums, 2))