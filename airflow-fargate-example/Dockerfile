FROM python:3.6-slim

ENV USER_HOME=/usr/local/ishan
COPY . ${USER_HOME}/app
WORKDIR ${USER_HOME}/app
RUN pip install -r ${USER_HOME}/app/requirements.txt

CMD ["python","myCode.py", "Ishan"]