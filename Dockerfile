FROM python:3.10-slim-buster

LABEL Name="Python Key-Value Storage App + API"

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY $srcDir/run.py .
COPY $srcDir/app ./app

EXPOSE 5000

CMD [ "uvicorn", "app.run:app", "--reload" ]