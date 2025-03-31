def median(arr1, arr2):
    merged = merge(arr1, arr2)

    if len(merged) % 2 != 0:
        return merged[len(merged) // 2]

    else:
        left = len(merged) // 2 - 1
        right = len(merged) // 2

        return ( merged[left] + merged[right] ) / 2


def merge(a, b):
    i = 0
    j = 0
    
    s = []

    while i < len(a) or j < len(b):
        if i == len(a):
            for ele in b[j:]:
                s.append(ele)
            break

        if j == len(b):
            for ele in a[i:]:
                s.append(ele)

            break


        if a[i] < b[j]:
            s.append(a[i])
            i += 1

        else:
            s.append(b[j])
            j += 1

    return s



nums1 = [1,2] 
nums2 = [3,4]

print(median(nums1, nums2))



        

