FROM python:2.7.13
MAINTAINER "shraddhayeole15@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -r github.txt
ENTRYPOINT ["python", "app.py"]
CMD [$1]
