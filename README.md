# NMS
This is a simple implementation of NMS (Non maximum suppression) algorithm. It takes a csv file containing potencial detections with their scores and computes nms algorithm writing the result on an output file.

# Requirements
* **Docker**: 18.06.1-ce or greater

# Installation

This project builds a docker image containing all dependencies needed. To build the docker image please execute:
```
docker build -t detection/nms .
```
# Execute
To execute, after compiling docker image:
```
docker run -v $PWD/examples:/examples detection/nms -i /examples/example_1.csv -o /examples/output.csv -t 0.1
```
Algorithms results will be available on examples/output.csv

