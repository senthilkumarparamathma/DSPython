class ArithmeticExpression:
    def __init__(self):
        self.stackOperator = []
        self.stackNumber = []

    def evaluateExpression(self, expression):

        for letter in expression:
            if letter.isdigit():
                self.stackNumber.append(letter)
            else:
                self.stackOperator.append(letter)

            if len(self.stackNumber) == 2:
                self.compute()

    def compute(self):
        num2 = self.stackNumber.pop()
        num1 = self.stackNumber.pop()
        operator = self.stackOperator.pop()

        if operator == "+":
            self.stackNumber.append(int(num1) + int(num2))
        elif operator == "-":
            self.stackNumber.append(int(num1) - int(num2))

    def getResult(self):
        print(self.stackNumber.pop())


ae = ArithmeticExpression()
ae.evaluateExpression("5-5+3")
ae.getResult()