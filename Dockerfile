FROM python:3.8 
WORKDIR /src
RUN apt update -y && \
    apt upgrade -y
COPY ./Pipfile /src/
RUN pip install pipenv && \
    pipenv install

COPY ./src /src
COPY ./.env /src
CMD ["pipenv", "run", "./main.py"]