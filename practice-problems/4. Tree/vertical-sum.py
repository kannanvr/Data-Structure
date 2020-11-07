def helper(root, idx, hashMap):
    if root is None:
        return
    try:
        # hashMap[idx].append(root.data)
        hashMap[idx] += root.data
    except KeyError:
        # hashMap[idx] = [root.data]
        hashMap[idx] = root.data

    helper(root.left, idx - 1, hashMap)
    helper(root.right, idx + 1, hashMap)


# Complete the function below
def verticalSum(root):
    #:param root: root of the given tree.

    hashMap = dict()
    helper(root, 0, hashMap)
    # print(hashMap)
    arr = []
    for k in hashMap.keys():
        arr.append(k)
        arr.sort()

    for value in arr:
        print(hashMap[value], end=" ")

