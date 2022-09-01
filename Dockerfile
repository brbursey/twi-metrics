FROM python:3.10-slim-bullseye

RUN apt-get update

RUN pip install -U pip

COPY ./requirements.txt ./code/requirements.txt

RUN python3 -m venv /venv

RUN pip install --no-compile -r /code/requirements.txt

RUN     mkdir -vp /code ; \
    apt -qq -y update && \
    apt -qq -y upgrade && \
    apt -qq -y autoremove && \
    rm -rf /var/lib/dpkg/info/* /var/lib/apt/lists/*

COPY . /code/

WORKDIR /code

CMD ["python", "main.py"]