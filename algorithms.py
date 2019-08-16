from typing import List
from detection import Detection
from utils import get_max_score_detection


def nms(detections: List[Detection], nms_threshold: float,
        not_suppress: bool = False) -> List[Detection]:
    remaining_detections = list(detections)
    detections_result = list()
    while remaining_detections:
        max_scored_detection = get_max_score_detection(remaining_detections)
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
