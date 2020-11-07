def floorSqrt(x):
    # Your code here
    c = 1
    while c * c <= x:
        c += 1
    return c - 1


def floorSqrt1(x):
    s, e, ans = 0, x, -1
    while s <= e:
        mid = (s + e) // 2
        if mid * mid == x:
            ans = mid
            break
        if mid * mid < x:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans
