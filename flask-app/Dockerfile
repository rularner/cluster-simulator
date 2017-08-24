FROM python:3.4
ADD requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
CMD ["flask", "run", "--host=0.0.0.0"]
