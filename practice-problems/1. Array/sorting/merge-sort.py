# {38, 27, 43, 3, 9, 82, 10}.

def merge(arr1, arr2):
    tmp = [0] * (len(arr1) + len(arr2))
    i, j, c = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            tmp[c] = arr1[i]
            i += 1
        else:
            tmp[c] = arr2[j]
            j += 1
        c += 1
    while i < len(arr1):
        tmp[c] = arr1[i]
        i += 1
        c += 1
    while j < len(arr2):
        tmp[c] = arr2[j]
        j += 1
        c += 1
    return tmp


def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    if len(arr) > 1:
        m = len(arr) // 2
        l = mergeSort(arr[:m])
        r = mergeSort(arr[m:])
        return merge(l, r)


print(mergeSort([3, 1, 6, 4, 9]))
print(mergeSort([999,612,589,856,56,945,243]))
print(mergeSort([12, 11, 13, 5, 6, 7]))
