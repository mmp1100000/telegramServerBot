FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./controller.py ./
COPY ./main ./main

CMD [ "python", "./controller.py" ]