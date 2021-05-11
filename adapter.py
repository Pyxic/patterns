from math import sqrt


class RoundHole:

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def fits(self, peg):
        return self.radius >= peg.radius


class RoundPeg:

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius


class SquarePeg:

    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side


class SquareAdapter(RoundPeg):

    def __init__(self, square_peg):
        self.square_peg = square_peg

    @property
    def radius(self):
        return self.square_peg.side * sqrt(2)/2


hole = RoundHole(5)
rpeg = RoundPeg(5)
print(hole.fits(rpeg))

small_sqpeg = SquarePeg(5)
large_sqpeg = SquarePeg(10)

small_sqpeg_adapter = SquareAdapter(small_sqpeg)
large_sqpeg_adapter = SquareAdapter(large_sqpeg)
print(hole.fits(small_sqpeg_adapter))
print(hole.fits(large_sqpeg_adapter))


