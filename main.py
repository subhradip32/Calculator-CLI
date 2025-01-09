import  os 
import time 
import math

class Calculator:
    '''
    Creating a Calculator object and helping us solving few basic mathematical operations
    like=> Add, Sub, Multiplication etc.
    '''

    # Constructor 
    def __init__(self):
        pass

    def add(self, a: float, b: float):
        '''Returns the addition of the provided a and b variables.'''
        return a + b  

    def sub(self, a: float, b: float):
        '''Returns the subtraction of the provided a and b variables.'''
        return a - b

    def mul(self, a: float, b: float):
        '''Returns the multiplication of the provided a and b variables.'''
        return a * b
    
    def div(self, a: float, b: float):
        '''Returns the division of the provided a and b variables.'''
        if b == 0:
            return None
        return a / b


# Handle CLI
class CLI:
    def __init__(self):
        self.clear_screen()
        self.counter = 21
        self.data = ""
        self.expression = " " * self.counter
        self.display = "  " + self.expression + "  "
        self.numbers = []
        self.operations = []

    def clear_screen(self):
        os.system("cls")
    
    def is_integer(self,s: str):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def addExpressionToDisplay(self, inp: str):
        if self.is_integer(inp):
            self.numbers.append(float(inp))
        else:
            self.operations.append(inp)

        self.counter -= len(inp.strip())
        self.data = self.data + inp
        self.expression = " " * self.counter + self.data
        self.display = "  " + self.expression + "  "

    def clearDisplay(self):
        self.counter = 21
        self.data = ""
        self.expression = " " * self.counter
        self.display = "  " + self.expression + "  "
        self.numbers = []
        self.operations = []
        self.calculator_replica()

    def calExpression(self):
        '''Calculate the output of the expression using the Calculator object.'''
        calcu = Calculator()

        # First, handle multiplication and division, as they have higher precedence
        while '*' in self.operations or '/' in self.operations:
            for i in range(len(self.operations)):
                if self.operations[i] == '*' or self.operations[i] == '/':
                    op = self.operations[i]
                    a = self.numbers[i]
                    b = self.numbers[i + 1]

                    # Perform the operation
                    if op == '*':
                        result = calcu.mul(a, b)
                    elif op == '/':
                        result = calcu.div(a, b)

                    # Replace the operands and operator with the result
                    self.numbers[i] = result
                    del self.numbers[i + 1]
                    del self.operations[i]
                    break

        # Now, handle addition and subtraction
        result = self.numbers[0]
        for i in range(len(self.operations)):
            op = self.operations[i]
            b = self.numbers[i + 1]

            if op == '+':
                result = calcu.add(result, b)
            elif op == '-':
                result = calcu.sub(result, b)

        # Set the result in the display
        self.clearDisplay()
        self.addExpressionToDisplay(str(result))

    def calculator_replica(self):
        """Displays a basic calculator replica in the terminal."""
        self.clear_screen()
        print("===================================")
        print("|         BASIC CALCULATOR        |")
        print("===================================")
        print("|   _________________________     |")
        print("|  |                         |    |")
        print(f"|  |{self.display}|    |")  # Display area
        print("|  |_________________________|    |")
        print("|  | 7  | 8  | 9  |  /  |    |    |")
        print("|  |----|----|----|-----|    |    |")
        print("|  | 4  | 5  | 6  |  *  |    |    |")
        print("|  |----|----|----|-----|    |    |")
        print("|  | 1  | 2  | 3  |  -  |    |    |")
        print("|  |----|----|----|-----|    |    |")
        print("|  | 0  |  . | =  |  +  |    |    |")
        print("|  |----|----|----|-----|  C |    |")
        print("===================================")


# Running the main code
cal_app = CLI()
flag = True
while flag:
    cal_app.calculator_replica()
    inp = input("Enter: ")

    if inp.lower() == "c":
        cal_app.clearDisplay()
        continue
    elif inp == "=":
        cal_app.calExpression()
    elif inp.lower() == "exit":
        flag = False 
    else:
        cal_app.addExpressionToDisplay(inp)
