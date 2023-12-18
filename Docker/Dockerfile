# Use the latest python docker base
FROM python:latest

# Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
COPY *.py ./

# Installing required packages
RUN pip install machine

# Running the script
CMD [ "python","./main.py" ]