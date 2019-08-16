from typing import List
from detection import Detection
from exceptions import NmsThresholdInvalidException
from utils import get_max_score_detection


def nms(detections: List[Detection], nms_threshold: float,
        not_suppress: bool = False) -> List[Detection]:
    """
    non maximum suppression algorithm implementation
    :param detections: list of detections
    :param nms_threshold: nms threshold. This value must be between 0.0 and 1.0
    :param not_suppress: If this boolean is true
                         algorithm sets to zero bad detections
                         instead of erase them.
    :return: list of filtered detections
    """
    remaining_detections = list(detections)
    detections_result = list()
    if nms_threshold < 0.0 or nms_threshold > 1.0:
        raise NmsThresholdInvalidException()
    while remaining_detections:
        max_scored_detection = get_max_score_detection(remaining_detections)
        assert max_scored_detection is not None
        detections_result.append(max_scored_detection)
        remaining_detections.remove(max_scored_detection)
        for detection in remaining_detections:
            iou = max_scored_detection.bounding_box.iou(
                detection.bounding_box)
            if iou >= nms_threshold:
                remaining_detections.remove(detection)
                if not_suppress:
                    detection.score = 0.0
                    detections_result.append(detection)
    return detections_result
