class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None
       // this is a node of the tree , which contains info as data, left , right
'''


# Method 1 (By Storing root to n1 and root to n2 paths): https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
# Following is simple O(n) algorithm to find LCA of n1 and n2.
# 1) Find path from root to n1 and store it in a vector or array.
# 2) Find path from root to n2 and store it in another vector or array.
# 3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.

def searchNode(root, key, arr):
    if root.info == key:
        return root
    if key < root.info:
        arr.append(root.left)
        return searchNode(root.left, key, arr)
    if key > root.info:
        arr.append(root.right)
        return searchNode(root.right, key, arr)


def lca(root, v1, v2):  # time O(n) and space O(hv1+hv2)
    arr1, arr2 = [root], [root]  # arr1 keep path from root to v1 and arr2 keep track of path from root to v2
    node_v1 = searchNode(root, v1, arr1)
    # print(arr1)
    node_v2 = searchNode(root, v2, arr2)
    # print(arr2)
    if len(arr1) == 1 or len(arr2) == 1:
        return arr1[0]
    if len(arr1) < len(arr2):
        for i in range(1, len(arr1)):
            if arr1[i] != arr2[i]:
                return arr1[i - 1]
        return arr1[-1]  # for case a1=[8,4,1] a2=[8,4,1,2]
    else:
        for i in range(1, len(arr2)):
            if arr1[i] != arr2[i]:
                return arr1[i - 1]
        return arr2[-1]


# -----------------------LCA in O(n) and O(1); https://www.youtube.com/watch?v=13m9ZCB8gjw&t=103s
def findLCA(root, n1, n2):
    # Base Case
    if root is None:
        return None
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root
    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


# ------------------------------------------------
def lca(r, v1, v2):
    if r.info > v1 and r.info > v2:
        return lca(r.left, v1, v2)  # LCA exist in left subtree
    if r.info < v1 and r.info < v2:
        return lca(r.right, v1, v2)  # LCA exist in right subtree
    return r


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
v = list(map(int, input().split()))
ans = lca(tree.root, v[0], v[1])
print(ans.info)
