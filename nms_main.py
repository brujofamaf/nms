import os
import sys
import argparse
from exceptions import NmsException
from io_ops import detections_from_csv, detections_to_csv
from algorithms import nms


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Non Maximum Suppression algorithm")
    arg_parser.add_argument("-i", "--detections-file",
                            help="Detections csv file path",
                            type=str,
                            required=True)
    arg_parser.add_argument("-o", "--output-file",
                            help="Detections filteres csv output file path",
                            type=str,
                            default="./output.csv",
                            required=False)
    arg_parser.add_argument("-t", "--nms-threshold",
                            help="Nms threhold",
                            type=float,
                            default=0.5,
                            required=False)
    arg_parser.add_argument("-s", "--not_suppress",
                            help="If present it won't be delete "
                                 "suppressed ones. Just set score to zero",
                            action='store_true')
    parsed_args = arg_parser.parse_args()
    try:
        input_file = os.path.abspath(parsed_args.detections_file)
        detections = detections_from_csv(input_file)
        filtered_detections = nms(detections, parsed_args.nms_threshold,
                                  parsed_args.not_suppress)
        detections_to_csv(parsed_args.output_file, filtered_detections)
    except NmsException as e:
        print("A problem occurs when executing nms: {}".format(str(e)),
              file=sys.stderr)
    except Exception as e:
        print("Unknown detected error: {}".format(str(e)), file=sys.stderr)
