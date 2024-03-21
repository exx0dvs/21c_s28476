import math
from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, begin, end):
        pass

    def calculate_square_roots(self, squares_list):
        return [math.sqrt(x) for x in squares_list]