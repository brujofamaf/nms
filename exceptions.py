class NmsException(Exception):
    """
    Represents a Nms base exception
    """
    def __init__(self, msg=""):
        """
        Default constructor
        """
        self._msg = msg
        super(NmsException, self).__init__(self)

    def __str__(self):
        """
        Returns the exception message
        """
        return self._msg


class NegativeCoordinateException(NmsException):
    """
    Exception thrown when user tries to instantiate a negative coordinate
    """
    def __init__(self):
        super(NegativeCoordinateException, self).__init__(
            "Coordinate x or y cannot be Negative")
