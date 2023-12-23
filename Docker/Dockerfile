#! Use the latest python docker base
FROM python:latest
#* Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
#*Adding API KEY
RUN --mount=type=secret,id=API,target=/usr/app/src/secret.txt echo /usr/app/src/secret.txt
COPY ./Docker/main.py ./
#* running it
CMD [ "python","./main.py"]c:\02_PXL\IoT_Technologie_PXL_2024\Docker\Dockerfile