from exceptions import NegativeCoordinateException


class Coordinate(object):
    """
    represents a linear positive coordinate
    """

    def __init__(self, x: int, y: int):
        """
        Coordinate class constructor
        :param x: horizontal coordinate
        :param y: vertical coordinate
        """
        if x < 0 or y < 0:
            raise NegativeCoordinateException()
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """
        gets x coordinate
        :return: x coordinate
        """
        return self._x

    @property
    def y(self) -> int:
        """
        gets y coordinate
        :return: y coordinate
        """
        return self._y

    def __str__(self) -> str:
        """
        coordinate string representation
        :return: string representation
        """
        return "({x},{y})".format(x=self._x, y=self._y)
