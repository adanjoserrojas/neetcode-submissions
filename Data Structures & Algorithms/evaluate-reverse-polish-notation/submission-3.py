import math
import operator

class Solution:
    operator_map = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        if len(tokens) == 1 and tokens[0] not in self.operator_map:
            return int(tokens[0])

        for value in tokens:
            if (
                len(stack) >= 2 and
                value == "+" or 
                value == "-" or
                value == "*" or
                value == "/"
            ):
                a = int(stack.pop())
                b = int(stack.pop())
                calc_func = self.operator_map[value]
                c = calc_func(b, a)
                stack.append(c)

            else:
                stack.append(value)
        
        return int(stack[0])
        
