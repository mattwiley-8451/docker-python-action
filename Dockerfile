FROM python:3.9.7-slim

COPY entrypoint.sh /action/entrypoint.sh
COPY requirements.txt /action/requirements.txt
COPY main.py /action/main.py

RUN chmod +x /action/*

RUN pip install -U pip && \
    pip install -r /action/requirements.txt

ENTRYPOINT [ "/action/entrypoint.sh" ]