# Use the latest python docker base
FROM python:latest

RUN apt-get update && apt-get install -y \
    python3-rpi.gpio
RUN pip install RPi.GPIO
# Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
COPY *.py ./

# Installing required packages
#RUN upip install micropython-machine

# Running the script
CMD [ "python","./main.py" ]