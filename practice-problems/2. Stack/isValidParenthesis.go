package stack
func isValid(s string) bool {
	var c int
	var stack = make([]string, 0)
	for _, ch:=range s{
		v :=string(ch)
		if v=="(" || v=="[" || v=="{" {
			stack=append(stack,v)
			c++
		} else{
			//if stack starts with closing braces eg. "]"
			if c==0 {
				return false
			}
			if v==")" && stack[c-1] != "("{
				return false
			}
			if v=="}" && stack[c-1] != "{"{
				return false
			}
			if v=="]" && stack[c-1] != "["{
				return false
			}
			//if top of the stack is matched opening braces then pop it
			stack=stack[:c-1]
			c--
		}
	}

	if len(stack)==0{ //if number of openings braces more than closing barces eg: ((())
		return true
	}
	return false

}

/*
   def isValid(self, s: str) -> bool:
       stack=[]
       for ch in s:
           if ch in ['{','(','[']:
               stack.append(ch)
           elif ch==')' and len(stack)>0 and stack[-1] == '(':
               stack.pop()
           elif ch==']' and len(stack)>0 and stack[-1]=='[':
               stack.pop()
           elif ch=='}' and len(stack)>0 and stack[-1] =='{':
               stack.pop()
           else:
               return False
       if len(stack)==0:
           return True
       return False

*/