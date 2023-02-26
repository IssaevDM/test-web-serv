FROM python:3.11.1-slim-bullseye
RUN apt -y update && apt -y upgrade
RUN apt -y install curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config virtualenvs.create false
WORKDIR /flask_docker
COPY ./pyproject.toml ./
COPY ./*.py ./flask_docker/
COPY ./README.md ./
RUN poetry install
ENV FLASK_APP=flask_docker
ENTRYPOINT ["waitress-serve", "--host=0.0.0.0", "flask_docker:app"] 
