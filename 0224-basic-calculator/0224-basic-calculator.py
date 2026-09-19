class Solution:
    def calculate(self, s: str) -> int:
        operators = []
        postfix = []

        i = 0
        n = len(s)

        # Infix → Postfix
        while i < n:

            if s[i] == ' ':
                i += 1
                continue

            # Number
            if s[i].isdigit():
                num = 0

                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                postfix.append(num)

            # Opening parenthesis
            elif s[i] == '(':
                operators.append('(')
                i += 1

            # Closing parenthesis
            elif s[i] == ')':
                while operators and operators[-1] != '(':
                    postfix.append(operators.pop())

                operators.pop()       # remove '('
                i += 1

            # + or -
            else:
                op = s[i]

                # Find previous non-space character
                j = i - 1

                while j >= 0 and s[j] == ' ':
                    j -= 1

                # Unary + or -
                if op in '+-':
                    if j < 0 or s[j] == '(' or s[j] in '+-':
                        postfix.append(0)

                # Pop previous operators
                while operators and operators[-1] != '(':
                    postfix.append(operators.pop())

                operators.append(op)
                i += 1

        # Remaining operators
        while operators:
            postfix.append(operators.pop())

        # Evaluate Postfix
        stack = []

        for token in postfix:

            if isinstance(token, int):
                stack.append(token)

            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                else:
                    stack.append(a - b)

        return stack[-1]