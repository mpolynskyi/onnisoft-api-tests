FROM python:3.7.2-alpine

COPY requirements.txt /tmp
RUN pip install --requirement /tmp/requirements.txt

CMD [ "python", "-m", "pytest", "-p", "no:warnings", "--show-progress" ]