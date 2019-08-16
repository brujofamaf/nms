from coordinate import Coordinate
from exceptions import NegativeValueException, InvalidBoundingBox


class BoundingBox(object):
    """
    Represents a bounding box
    """

    def __init__(self, top_right_coordinate: Coordinate,
                 width: int, height: int):
        """
        class constructor
        :param top_right_coordinate: top right coordinate of bounding box
        :param width: bounding box width
        :param height: bounding box height
        """
        self._top_right_coord = top_right_coordinate
        if width < 0:
            raise NegativeValueException("bounding box width")
        if height < 0:
            raise NegativeValueException("bounding box height")
        if top_right_coordinate.x - width < 0:
            raise InvalidBoundingBox(top_right_coordinate, width, height)
        self._width = width
        self._height = height

    @property
    def w(self) -> int:
        """
        returns bounding box width
        :return: bounding box width
        """
        return self._width

    @property
    def h(self) -> int:
        """
        returns bounding box height
        :return: bounding box height
        """
        return self._height

    @property
    def top_left_coordinate(self) -> Coordinate:
        """
        calculates top left coordinate of bounding box
        :return: top left coordinate
        """
        return Coordinate(self._top_right_coord.x - self._width,
                          self._top_right_coord.y)

    @property
    def bottom_right_coordinate(self) -> Coordinate:
        """
        returns bottom right coordinate
        :return: bottom right coordinate
        """
        return Coordinate(self._top_right_coord.x,
                          self._top_right_coord.y + self._height)

    def iou(self, bb2) -> float:
        """
        returns intersection over union between self nd bb2
        :param bb2: bounding box 2
        :type: BoundingBox
        :return: intersection over union 0 <= iou <= 1
        """
        bb1_top_left = self.top_left_coordinate
        bb1_bottom_right = self.bottom_right_coordinate
        bb2_top_left = bb2.top_left_coordinate
        bb2_bottom_right = bb2.bottom_right_coordinate
        assert bb1_top_left.x < bb1_bottom_right.x
        assert bb1_top_left.y < bb1_bottom_right.y
        assert bb2_top_left.x < bb2_bottom_right.x
        assert bb2_top_left.y < bb2_bottom_right.y

        # determine the coordinates of the intersection rectangle
        x_left = max(bb1_top_left.x, bb2_top_left.x)
        y_top = max(bb1_top_left.y, bb2_top_left.y)
        x_right = min(bb1_bottom_right.x, bb2_bottom_right.x)
        y_bottom = min(bb1_bottom_right.y, bb2_bottom_right.y)

        if x_right < x_left or y_bottom < y_top:
            return 0.0

        # The intersection of two axis-aligned bounding boxes is always an
        # axis-aligned bounding box
        intersection_area = (x_right - x_left) * (y_bottom - y_top)

        # compute the area of both AABBs
        bb1_area = (bb1_bottom_right.x - bb1_top_left.x) * (
            bb1_bottom_right.y - bb1_top_left.y)
        bb2_area = (bb2_bottom_right.x - bb2_top_left.x) * (
            bb2_bottom_right.y - bb2_top_left.y)

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the intersection area
        iou = intersection_area / float(
            bb1_area + bb2_area - intersection_area)
        assert 0.0 <= iou <= 1.0  # it should not happen.
        return iou
