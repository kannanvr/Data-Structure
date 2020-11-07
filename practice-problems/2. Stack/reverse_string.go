package stack
type myStack []rune

func (s myStack) Push(v rune) myStack {
	return append(s, v)
}

func (s myStack) Pop() (myStack, rune) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func (s myStack) isEmpty() bool {
	return len(s) == 0
}

func reverseString(str string) (string) {
	rtsRunes := []rune{}
	strRunes := []rune(str)
	stack := myStack{}
	for i := 0; i < len(strRunes); i++ {
		stack = stack.Push(strRunes[i])
	}
	for !stack.isEmpty() {
		var r rune
		stack, r = stack.Pop()
		rtsRunes = append(rtsRunes, r)
	}

	return string(rtsRunes)
}
