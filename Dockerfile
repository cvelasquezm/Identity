from python:3.10-slim as base
COPY ./identity /code/app
WORKDIR /code
ENV LOGIN_PORT=8080


FROM base as dev
RUN pip install --no-cache-dir --upgrade -r /code/app/config/requirements.txt
RUN pip install 'pydantic[email]'
CMD uvicorn identity.main:api --host 0.0.0.0 --port ${LOGIN_PORT} --reload
