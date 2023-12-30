# Use the latest python docker base
FROM python:latest

#adding libraries
RUN pip install requests urllib3
RUN pip install spidev


# Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
COPY *.py ./

#*Adding API KEY
RUN --mount=type=secret,id=API,target=/usr/app/src/secret cat /usr/app/src/secret > ./secretfile.txt
RUN --mount=type=secret,id=API,target=/usr/app/src/secret API=$(cat /usr/app/src/secret)
ENV API_KEY=$API

#* running it
CMD ["python", "./main.py", "ARGUMENT"]
