# NMS
This is a simple implementation of NMS (Non maximum suppression) algorithm. It takes a csv file containing potencial detections with their scores and computes nms algorithm writing the result on an output file.

# Requirements
* **Docker**: 18.06.1-ce or greater

# Installation

This project builds a docker image containing all dependencies needed. To build the docker image please execute:
```
docker build -t detection/nms .
```
If docker image was built correctly you will be able to execute:

```
docker run -v  detection/nms --help
```
Producing the following output:
```
usage: nms_main.py [-h] -i DETECTIONS_FILE [-o OUTPUT_FILE] [-t NMS_THRESHOLD]
                   [-s]

Non Maximum Suppression algorithm

optional arguments:
  -h, --help            show this help message and exit
  -i DETECTIONS_FILE, --detections-file DETECTIONS_FILE
                        Detections csv file path
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Detections filteres csv output file path
  -t NMS_THRESHOLD, --nms-threshold NMS_THRESHOLD
                        Nms threhold
  -s, --not_suppress    If present it won't be delete suppressed ones. Just
                        set score to zero
```

# Execute
To execute the example, after builds docker image:
```
docker run -v $PWD/examples:/examples detection/nms -i /examples/example_1.csv -o /examples/output.csv -t 0.1
```
Algorithms results will be available on examples/output.csv

To execute another example use:

```
docker run -v <your_system_input_folder>:/input -v <your_system_output_folder>:/output  detection/nms -i /input/<input_file> -o /output/<output_file> -t <threshold>
```
