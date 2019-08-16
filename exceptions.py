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


class NegativeValueException(NmsException):
    """
    Exception thrown when tries to instantiate a negative int value
    """
    def __init__(self, variable_name):
        super(NegativeValueException, self).__init__(
            "{variable_name} cannot be Negative".format(
                variable_name=variable_name))


class InvalidBoundingBox(NmsException):
    """
    Exception thrown when tries to instantiate an invalid bounding box
    """

    def __init__(self, coord, w, h):
        super(InvalidBoundingBox, self).__init__(
            "Invalid bounding box: {{coord}, {w}, {h}".format(
                coord=coord, w=w, h=h))


class ScoreNotValid(NmsException):
    """
    Exception thrown when detection score is not valid
    """

    def __init__(self):
        super(ScoreNotValid, self).__init__(
            "Detection score must be between 0.0 and 1.0")


class NmsThresholdInvalidException(NmsException):
    """
    Exception thrown when nms threshold value is not valid
    """

    def __init__(self):
        super(NmsThresholdInvalidException, self).__init__(
            "Nms threshold must be between 0.0 and 1.0")
