FROM python:3.9.0
RUN mkdir /workspace
WORKDIR /workspace
COPY . /workspace/
RUN pip install -r requirements.txt
