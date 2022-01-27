def evaluate(operands, operator):
    if operator == "+":
        return int(operands[0]) + int(operands[1])
    elif operator == "-":
        return int(operands[0]) - int(operands[1])
    elif operator == "*":
        return int(operands[0]) * int(operands[1])
    elif operator == "/":
        return int(operands[0]) / int(operands[1])
    elif operator == "^":
        return int(operands[0]) ** int(operands[1])


precedence = {"X": -1, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

operator_stack, operand_stack = [], []

expression = list(str(input("Please enter an expression: ")).replace(" ", ""))
# 2 + 3 * 5 - 9 / 3 + 2 ^ 3

operand_stack.append(expression.pop(0))
operator_stack.append(expression.pop(0))
operand_stack.append(expression.pop(0))

while len(expression) > 0:
    next_operator = expression[0]
    if operator_stack and precedence[next_operator] > precedence[operator_stack[-1]]:
        operator_stack.append(expression.pop(0))
        operand_stack.append(expression.pop(0))
    elif not operator_stack:
        operator_stack.append(expression.pop(0))
        operand_stack.append(expression.pop(0))
    else:
        if len(operator_stack) > 1:
            temp_ans = evaluate(operand_stack[1:], operator_stack.pop())
        else:
            temp_ans = evaluate(operand_stack, operator_stack.pop())
        del operand_stack[-2:]
        operand_stack.append(temp_ans)
    if not expression:
        next_operator = "X"

if len(expression) % 2 == 0:
    if len(operator_stack) > 1:
        temp_ans = evaluate(operand_stack[1:], operator_stack.pop())
        del operand_stack[-2:]
        operand_stack.append(temp_ans)
        print(operand_stack)
        final_ans = evaluate(operand_stack, operator_stack.pop())
    else:
        final_ans = evaluate(operand_stack, operator_stack.pop())
    print("Final Answer:", final_ans)
else:
    print("Error: Invalid Expression")
