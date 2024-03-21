from task10.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, begin, end):
        if end < begin:
            raise ValueError("End of range must be greater than or equal to the start.")
        return [x ** 2 for x in range(begin, end + 1)]