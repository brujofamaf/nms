from typing import List
from detection import Detection


def get_max_score_detection(detections: List[Detection]) -> Detection:
    """
    get maximum scored detection of detections list
    :param detections: detections list
    :return: maximum scored detection.
             If detections is empty it will return None
    """
    max_detection = None
    max_score = 0.0
    for detection in detections:
        if detection.score > max_score:
            max_score = detection.score
            max_detection = max_detection
    return max_detection
