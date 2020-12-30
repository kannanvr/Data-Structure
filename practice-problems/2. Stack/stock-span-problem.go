package stack
/*
https://www.geeksforgeeks.org/the-stock-span-problem/
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

===Py Version===O(n*n)
t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        span,c=1,i-1
        while c>=0 and a[c]<=a[i]:
            span+=1
            c-=1
        print(span,end=' ')
    print()
    t-=1



----->use stack to solve in linear time
#code
t=int(input())
while t>0:
    n=int(input())
    price=list(map(int,input().split()))
    # Create a stack and push index of fist element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    print(1, end=' ')

    # Calculate span values for rest of the elements
    for i in range(1, n):

        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while( len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i] is
        # greater than elements after top of stack
        span = i + 1 if len(st) <= 0 else (i - st[-1])
        print(span,end=' ')

        # Push this element to stack
        st.append(i)
    print()
    t-=1

*/


