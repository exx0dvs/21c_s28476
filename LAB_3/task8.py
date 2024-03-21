# Packages

from task8.cubic_generator import CubicGenerator

firstNum = 1
secondNum = 10
generator = CubicGenerator()

print("Squares")
listOfSquares = generator.generate_squares(firstNum, secondNum)
listOfRoots = generator.calculate_square_roots(listOfSquares)
print(listOfSquares)
print(listOfRoots)

print("\nCubes")
listOfCubes = generator.generate_cubes(firstNum, secondNum)
listOfCubeRoots = generator.calculate_cube_roots(listOfCubes)
print(listOfCubes)
print(listOfCubeRoots)
