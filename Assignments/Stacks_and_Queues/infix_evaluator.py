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


operator_stack, operand_stack = [], []

expression = list(str(input("Please enter an expression: ")).replace(" ", ""))


operand_stack.append(expression[0])
operand_stack.append(expression[2])

operator_stack.append(expression[1])

if len(expression) == 4:
    operand_stack.append(expression[3])

for i in range(3, len(expression)):
    if expression[i] in "+-*/^":
        operator_stack.append(expression[i])
    else:
        operand_stack.append(expression[i])

while len(operator_stack) != 0:
    operator = operator_stack.pop()
    print(operator, operand_stack, operator_stack)
    operands = [operand_stack.pop(), operand_stack.pop()]
    operand_stack.append(evaluate(operands, operator))

print(operand_stack[0])
