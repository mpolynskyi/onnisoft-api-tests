FROM python:3

WORKDIR /onnisoft

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY tests ./tests

CMD [ "python", "-m", "pytest", "-p", "no:warnings", "--show-progress" ]