#! Use the latest python docker base
FROM python:latest
#* Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
COPY *.py ./
#* running it
RUN "pip install machine"
CMD [ "python","./main.py" ]