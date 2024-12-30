FROM python:3.11.7

WORKDIR /code
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY bloknot ./bloknot

CMD ["python", "-m", "bloknot.runner", "--root-path", "/bloknot"]
