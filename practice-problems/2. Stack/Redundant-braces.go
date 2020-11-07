package stack
/*Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.
//http://geeksforgeeks.org/expression-contains-redundant-bracket-not/
Chech whether A has redundant braces or not.

Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.



Input Format

The only argument given is string A.
Output Format

Return 1 if string has redundant braces, else return 0.
For Example

Input 1:
A = "((a + b))"
Output 1:
1
Explanation 1:
((a + b)) has redundant braces so answer will be 1.

Input 2:
A = "(a + (a + b))"
Output 2:
0
Explanation 2:
(a + (a + b)) doesn't have have any redundant braces so answer will be 0.
approach:
1. if any opening braces or operators found then push it into stack
2. if closing braces found and top of stack consist closing braces then there is redundant braces. return 1
3. else pop all operators until closing braces founds
4. repeat step2 and step3 until all elements scanned
5. return 0

class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
        c,stack=0,[]
        while c<len(A):
            if A[c]=='(' or A[c]=='+' or A[c]=='-' or A[c]=='*' or A[c]=='/':
                stack.append(A[c])
            elif A[c]==')':
                if stack[-1]=='(':
                    return 1
                else:
                    while len(stack)>0 and stack[-1]!='(':
                        stack.pop()
                    stack.pop()
            c+=1
        return 0


*/