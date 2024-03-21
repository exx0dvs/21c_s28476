# Functions
def generate_squares(begin, end):
    return [x ** 2 for x in range(begin, end + 1)]


firstNum = 1
secondNum = 10
listOfSquares = generate_squares(firstNum, secondNum)
print(listOfSquares)
