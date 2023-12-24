#! Use the latest python docker base
FROM python:latest
#* Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
COPY ./Docker/main.py ./

#*Adding API KEY
RUN --mount=type=secret,id=API,target=/usr/app/src/secret cat /usr/app/src/secret > ./secretfile.txt
RUN --mount=type=secret,id=API,target=/usr/app/src/secret API=$(cat /usr/app/src/secret)
ENV API_KEY_FILE=/usr/app/src/secret
#adding libraries
RUN pip install requests

#* running it
CMD ["sh", "-c", "python /usr/app/src/main.py $(cat $API_KEY_FILE)"]c:\02_PXL\IoT_Technologie_PXL_2024\Docker\Dockerfile

#test CMD
# Create a JSON file with your data
RUN echo '{"id": "$(date +%s)", "value": 123.45, "scale": "F"}' > data.json
#CMD ["sh", "-c", "curl -X PUT -H 'X-Api-Key: $API_KEY' -d @data.json  iot.pxl.bjth.xyz/api/v1/temperature"]
# CMD [ "ls"]