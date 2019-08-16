FROM python:3.6
LABEL maintainer="brujofamaf@gmail.com"

WORKDIR /usr/src/app
COPY . .

CMD [ "python", "./nms_main.py" ]