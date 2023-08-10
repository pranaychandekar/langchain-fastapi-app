FROM python:3.11-slim

MAINTAINER Pranay Chandekar "pranayc6@gmail.com"

LABEL project="langchain-fastapi-app"

EXPOSE 8080

ARG APP_HOME=/opt/deployment
ARG PROJECT_NAME="langchain-fastapi-app"

ENV APP_HOME=${APP_HOME} \
    PROJECT_NAME=${PROJECT_NAME} \
    PROJECT_HOME=${APP_HOME}/${PROJECT_NAME}

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

ADD requirements.txt /

RUN pip3 install -r requirements.txt && \
    mkdir -p ${PROJECT_HOME}/src && \
    mkdir -p ${PROJECT_HOME}/logs && \
    mkdir -p ${PROJECT_HOME}/conf && \
    mkdir -p ${PROJECT_HOME}/resources

COPY src ${PROJECT_HOME}/src
COPY app.py ${PROJECT_HOME}/
COPY conf ${PROJECT_HOME}/conf
COPY resources ${PROJECT_HOME}/resources
COPY *-server.sh ${APP_HOME}/

RUN chmod a+x ${APP_HOME}/start-server.sh

WORKDIR ${PROJECT_HOME}
ENTRYPOINT ["/opt/deployment/start-server.sh"]