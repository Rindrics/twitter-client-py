FROM python:3.9-buster

WORKDIR /flask-docker

ENV POETRY_HOME=/opt/poetry

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY . /flask-docker

RUN poetry install

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]