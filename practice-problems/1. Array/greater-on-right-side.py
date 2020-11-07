def Greater_on_right_side(ar,n): #greatest element on its right side, not next greater element
    max_so_far=ar[n-1]
    next_max=[-1 for i in range(n)]
    for i in range(n-2,-1,-1):
        next_max[i]=max_so_far
        if ar[i]>max_so_far:
            max_so_far=ar[i]
    for i in range(n):
        print(next_max[i],end=' ')
    print()

#Next Greater Element use stack
'''
1. Push the first element to stack.
2. Pick rest of the elements one by one and follow the following steps in loop.
 a. Mark the current element as next.
 b. If stack is not empty, compare top element of stack with next.
 c. If next is greater than the top element,Pop element from stack. next is the next greater element for the popped element.
 d. Keep popping from the stack while the popped element is smaller than next. next becomes the next greater element for all such popped elements
3. Finally, push the next in the stack.
4. After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.
'''
#def count_greater_numbers_on_right_side(arr):