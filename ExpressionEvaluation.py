def precedence(ope):
    if ope == "+" or ope == "-":
        return 1
    elif ope == "*" or ope == "/":
        return 2
    else:
        return 0


def compute(value1, value2, operator):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 // value2


def evaluate(expression):
    valueStack = []
    operatorStack = []

    i = 0
    while i < len(expression):
        # print(valueStack)
        if expression[i] == ' ':
            i += 1
            continue

        if expression[i] == "(":  # open brace
            operatorStack.append(expression[i])
            # print(operatorStack)
        elif expression[i].isdigit():  # digit
            # valueStack.append(expression[i])
            valueString = expression[i]
            while i + 1 < len(expression) and expression[i + 1].isdigit():
                i += 1
                valueString = valueString + expression[i]
            # print(int(valueString))
            valueStack.append(int(valueString))
        elif expression[i] == ")":  # close brace

            while len(operatorStack) > 0 and operatorStack[-1] != "(":
                val2 = valueStack.pop()
                val1 = valueStack.pop()
                oper = operatorStack.pop()
                res = compute(val1, val2, oper)
                valueStack.append(res)

            # pop opening brace "("
            operatorStack.pop()

        else:  # operator
            while len(operatorStack) > 0 and precedence(operatorStack[-1]) >= precedence(expression[i]):
                val2 = valueStack.pop()
                val1 = valueStack.pop()
                oper = operatorStack.pop()
                res = compute(val1, val2, oper)
                valueStack.append(res)
            # add operator
            operatorStack.append(expression[i])

        i += 1

    while len(operatorStack) > 0 and len(valueStack) >= 2:
        val2 = valueStack.pop()
        val1 = valueStack.pop()
        oper = operatorStack.pop()
        res = compute(val1, val2, oper)
        valueStack.append(res)

    if len(operatorStack) > 0 and operatorStack[0] == "-":
        return "-" + str(valueStack[-1])
    return valueStack[0]


res = evaluate("(3 + ( 2 - 1 ) )")
print(res)
