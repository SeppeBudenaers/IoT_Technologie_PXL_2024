#! Use the latest python docker base
FROM python:latest
#* Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
#*Adding API KEY
RUN --mount=type=secret,id=API,target=/usr/app/src/secret ENV API_KEY=$(cat /usr/app/src/secret)
COPY ./Docker/main.py ./
#* running it
# Create a JSON file with your data
RUN echo '{"id": "$(date +%s)", "value": 123.45, "scale": "F"}' > data.json
#*CMD ["sh", "-c", "curl -X PUT -H 'X-Api-Key: $(cat /usr/app/src/secret)' -d @data.json  iot.pxl.bjth.xyz/api/v1/temperature"]
CMD [ "python","./main.py","$API_KEY"]c:\02_PXL\IoT_Technologie_PXL_2024\Docker\Dockerfile