#! Use the latest python docker base
FROM python:latest
#* Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
#*Adding API KEY
RUN --mount=type=secret,id=API,target= ./credentials
RUN cat ./credentials
COPY ./Docker/main.py ./
#* running it
CMD [ "python","./main.py" ]c:\02_PXL\IoT_Technologie_PXL_2024\Docker\Dockerfile