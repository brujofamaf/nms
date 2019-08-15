FROM python:3.6
LABEL maintainer="brujofamaf@gmail.com"

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./nms_main.py" ]