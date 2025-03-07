# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        operation = ["*","/","+","-"]
        for i  in tokens:
            if i == "/" and len(values):
                a = values.pop()
                b = values.pop()
                values.append(int(b/a))
            elif i == "*" and len(values):
                a = values.pop()
                b = values.pop()
                values.append(int(b*a))
            elif i == "+" and len(values):
                a = values.pop()
                b = values.pop()
                values.append(int(b+a))
            elif i == "-" and len(values):
                a = values.pop()
                b = values.pop()
                values.append(int(b-a))
            elif i not in operation:
                values.append(int(i))
            
        return values[0]