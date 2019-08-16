FROM python:3.6
LABEL maintainer="brujofamaf@gmail.com"

WORKDIR /usr/src/app
COPY . .

ENTRYPOINT [ "python", "./nms_main.py" ]