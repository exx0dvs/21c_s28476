import math


class SquareGenerator:
    def generate_squares(self, begin, end):
        return [x ** 2 for x in range(begin, end + 1)]

    def calculate_square_roots(self, squares_list):
        return [math.sqrt(x) for x in squares_list]
