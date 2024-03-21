# Classes
class SquareGenerator:
    def generate_squares(self, begin, end):
        return [x ** 2 for x in range(begin, end + 1)]


firstNum = 1
secondNum = 10
generator = SquareGenerator()
listOfSquares = generator.generate_squares(firstNum, secondNum)
print(listOfSquares)
