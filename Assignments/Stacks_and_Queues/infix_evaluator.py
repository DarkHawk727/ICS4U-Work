from typing import List


expression = list(str(input("Please enter an expression: ")).replace(" ", ""))

operator_stack, operand_stack = [], []

# 1. Push the first two numbers to the operand stack and the operator to the operator stack
# 2. 