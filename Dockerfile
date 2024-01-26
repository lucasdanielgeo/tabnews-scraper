FROM python:3.10.12-slim-bullseye

COPY ./requirements.txt /app/
COPY main.py /app/
WORKDIR /app

RUN pip install -r /app/requirements.txt
RUN chmod a+x main.py

ENTRYPOINT ["python", "./main.py"]