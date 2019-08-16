from bounding_box import BoundingBox
from exceptions import ScoreNotValid


class Detection(object):
    """
    represents a detection over image
    """

    def __init__(self, bounding_box: BoundingBox, score: float):
        """
        class constructor
        :param bounding_box: detection bounding box
        :param score: detection score
        """
        if score < 0.0 or score > 1.0:
            raise ScoreNotValid()
        self._bb = bounding_box
        self._score = score

    @property
    def score(self) -> float:
        """
        gets detection score
        :return: detection score
        """
        return self._score

    @property
    def bounding_box(self) -> BoundingBox:
        """
        returns detection bounding box
        :return: detection bounding box
        """
        return self._bb

    @score.setter
    def score(self, score_new_val):
        """
        sets new value for score
        :param score_new_val: new score value
        """
        if score_new_val > 1.0 or score_new_val < 0.0:
            raise ScoreNotValid()
        self._score = score_new_val
