FROM python:3.10-slim

ARG PROJECT_PATH=src

ENV FLASK_ENV=development

COPY ./${PROJECT_PATH}/requirements.txt /
RUN pip install -U pip && pip install -r requirements.txt

EXPOSE 5000

COPY ./${PROJECT_PATH}/app /app
COPY ./${PROJECT_PATH}/run.py /
COPY ./${PROJECT_PATH}/setup.py /

WORKDIR /

CMD gunicorn -c setup.py run:app