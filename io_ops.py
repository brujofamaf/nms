from typing import List
import csv
from detection import Detection
from coordinate import Coordinate
from bounding_box import BoundingBox

X_TOP_RIGHT_KEY = "x_top_right"
Y_TOP_RIGHT_KEY = "y_top_right"
BB_W = "bb_w"
BB_H = "bb_h"
SCORE = "score"
FIELDNAMES = [X_TOP_RIGHT_KEY, Y_TOP_RIGHT_KEY, BB_W, BB_H, SCORE]


def detections_from_csv(csv_filepath: str) -> List[Detection]:
    """
    reads a detection list from csv file
    :param csv_filepath: csv file path
    :return: detections list
    """
    detections = list()
    with open(csv_filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            top_right_coord = Coordinate(int(row[X_TOP_RIGHT_KEY]),
                                         int(row[Y_TOP_RIGHT_KEY]))
            bb = BoundingBox(top_right_coord, int(row[BB_W]), int(row[BB_H]))
            detection = Detection(bb, float(row[SCORE]))
            detections.append(detection)
    return detections


def detections_to_csv(csv_output_path: str, detections: List[Detection]):
    """
    writes detections into csv_output_path file
    :param csv_output_path: csv output path
    :param detections: detections
    """
    with open(csv_output_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)

        writer.writeheader()
        for detection in detections:
            top_right_coord = detection.bounding_box.top_right_coord
            detection_dict = {
                X_TOP_RIGHT_KEY: top_right_coord.x,
                Y_TOP_RIGHT_KEY: top_right_coord.y,
                BB_W: detection.bounding_box.w,
                BB_H: detection.bounding_box.h,
                SCORE: detection.score
            }
            writer.writerow(detection_dict)
