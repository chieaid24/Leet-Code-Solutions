class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # since you only need to access at most the last 2 elements we will use a stack
        # format to append to the record
        stack = []
        res = 0
        for op in operations:
            if op == "+":
                sum = stack[-1] + stack[-2]
                stack.append(sum)
                res += sum
            elif op == "D":
                double = stack[-1] * 2
                stack.append(double)
                res += double
            elif op == "C":
                res -= stack.pop()
            else:
                stack.append(int(op))
                res += int(op)
        return res