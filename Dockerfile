FROM public.ecr.aws/docker/library/alpine:3.14


RUN apk add py3-pip \
    && pip install --upgrade pip


RUN apk update && apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev

WORKDIR /app
COPY . /app/



RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "application.py"]

##Confguración New Relic
RUN pip install newrelic
ENV NEW_RELIC_APP_NAME="blacklists-forgate-app-local"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
#INGEST_License
ENV NEW_RELIC_LICENSE_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENV NEW_RELIC_LOG_LEVEL=info
# etc.

ENTRYPOINT ["newrelic-admin", "run-program"]