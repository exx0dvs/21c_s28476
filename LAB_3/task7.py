# Packages

from task7.square_generator import SquareGenerator

firstNum = 1
secondNum = 10
generator = SquareGenerator()
listOfSquares = generator.generate_squares(firstNum, secondNum)
listOfRoots = generator.calculate_square_roots(listOfSquares)
print(listOfSquares)
print(listOfRoots)
