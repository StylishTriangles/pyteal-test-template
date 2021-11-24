FROM python:3.9

WORKDIR /app

# Poetry cfg
RUN pip install poetry
# no need to create virtualenvs inside docker container
RUN poetry config virtualenvs.create false

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install

# pip cfg
# pip install -r requirements.txt
# or
# pip install -r requirements-dev.txt

COPY pytest.ini pytest.ini
COPY tests tests
# copy other stuff too...
