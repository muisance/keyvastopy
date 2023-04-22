FROM python:3.10-slim-buster

LABEL Name="Python Key-Value Storage App + API v0.4(-ish?)"

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY ${srcDir}/run.py .
COPY ${srcDir}/app ./app

EXPOSE 5000

ENTRYPOINT [ "uvicorn" ]

CMD [ "app.run:app", "--reload" ]