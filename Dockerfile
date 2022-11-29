# Dockerfile
FROM public.ecr.aws/docker/library/python:3.8.12-slim-buster

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.4.0 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /var/task

COPY requirements.txt  ./requirements.txt
RUN python -m pip install -r requirements.txt

COPY app.py  ./
COPY model/  ./model/
CMD ["python3", "app.py"]
