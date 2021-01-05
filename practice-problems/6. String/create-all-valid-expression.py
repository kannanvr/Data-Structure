class Solution:

    def _printParenthesis(self,str, pos, n,  open, close, result):

        if(close == n):
            result.append("".join(str))
            return result
        else:
            if(open > close):
                str[pos] = ')';
                result = self._printParenthesis(str, pos + 1, n,  open, close + 1, result);
            if(open < n):
                str[pos] = '(';
                result = self._printParenthesis(str, pos + 1, n,  open + 1, close, result);
        return result

    def printParenthesis(self,str, n):
        if(n > 0):
            result= self._printParenthesis(str, 0,  n, 0, 0, []);
        return result


    def generateParenthesis(self, n: int) -> List[str]:
        str = [""] * 2 * n;
        return self.printParenthesis(str, n);
