from task9.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, begin, end):
        if end < begin:
            return super().generate_squares(begin, end)
        return [x ** 2 for x in range(begin, end + 1)]

    def generate_cubes(self, begin, end):
        if end < begin:
            raise ValueError("End of range must be greater than or equal to the start.")
        return [x ** 3 for x in range(begin, end + 1)]

    def calculate_cube_roots(self, cubes_list):
        return [round(x ** (1/3), 10) for x in cubes_list]