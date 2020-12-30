package stack
/**
 * @input A : String
 *
 * @Output Integer
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
 */
type myStack []rune

func (s myStack) Push(v rune) myStack {
	return append(s, v)
}

func (s myStack) Pop() (myStack, rune) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func (s myStack) Peek() (rune) {
	l := len(s)
	return s[l-1]
}

func (s myStack) isEmpty() bool {
	return len(s) == 0
}

func isValid(str string) (int) {
	stack := myStack{}
	runes := []rune(str)
	for i := 0; i < len(runes); i++ {
		if runes[i] == '(' || runes[i] == '{' || runes[i] == '[' {
			stack = stack.Push(runes[i])
		}
		if runes[i] == ')' || runes[i] == '}' || runes[i] == ']' {
			if stack.isEmpty() {
				return 0
			} else if stack.Peek() != '(' && runes[i] == ')' {
				return 0
			} else if stack.Peek() != '{' && runes[i] == '}' {
				return 0
			} else if stack.Peek() != '[' && runes[i] == ']' {
				return 0
			} else {
				stack, _ = stack.Pop()
			}
		}
	}
	if !stack.isEmpty() {
		return 0
	}
	return 1
}