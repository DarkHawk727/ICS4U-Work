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


expression = list(str(input("Please enter an expression: ")).replace(" ", ""))

operator_stack, operand_stack = [], []


operand_stack.append(expression[0])
operand_stack.append(expression[2])

operator_stack.append(expression[1])


print(operand_stack)
print(operator_stack)


    