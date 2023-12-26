# Use the latest python docker base
FROM python:latest

#adding libraries
RUN apt-get update && apt-get install -y \
    python3-rpi.gpio
RUN pip install requests
RUN pip install RPi.GPIO

# Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
COPY *.py ./

#*Adding API KEY
RUN --mount=type=secret,id=API,target=/usr/app/src/secret cat /usr/app/src/secret > ./secretfile.txt
RUN --mount=type=secret,id=API,target=/usr/app/src/secret API=$(cat /usr/app/src/secret)
ENV API_KEY=$API
RUN echo $API_KEY


#* running it
CMD ["python", "./main.py", "ARGUMENT"]

#test CMD
# Create a JSON file with your data
# RUN echo '{"id": "$(date +%s)", "value": 123.45, "scale": "F"}' > data.json
# CMD ["sh", "-c", "curl -X PUT -H 'X-Api-Key: $API_KEY' -d @data.json  iot.pxl.bjth.xyz/api/v1/temperature"]
# CMD [ "ls"]