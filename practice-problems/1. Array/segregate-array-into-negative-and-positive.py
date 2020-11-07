def segregate(self, A):
    f = -1
    for i in range(len(A)):
        if A[i] < 0:
            f += 1
        A[f], A[i] = A[i], A[f]
    A[f + 1], A[i] = A[i], A[f + 1]
    return f


def segregate1(self, A):
    f, l = 0, len(A) - 1
    while f < l:
        if A[f] <= 0:
            f += 1
        if A[l] > 0:
            l -= 1
        elif A[f] > 0 and A[l] <= 0:
            A[f], A[l] = A[l], A[f]
            f += 1
            l -= 1
    print(A, f, l)


def segregate2(A):
    f, l = 0, len(A) - 1
    B = [0] * len(A)
    bf, bl = f, l
    while f < len(A) and l >= 0:
        if A[f] <= 0:
            B[bf] = A[f]
            bf += 1
        f += 1
        if A[l] > 0:
            B[bl] = A[l]
            bl -= 1
        l -= 1
    print(A, B, f, l)


a = [2, -1, 4, 5, -7, 0, 8, -5]
print(a)
segregate2(a)
