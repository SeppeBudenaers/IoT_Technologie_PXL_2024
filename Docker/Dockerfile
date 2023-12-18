# Use the latest python docker base
FROM micropython/build-micropython-arm

# Copying the main.py into the /usr/app/src/main.py
WORKDIR /usr/app/src
COPY *.py ./

# Installing required packages
RUN upip install micropython-machine

# Running the script
CMD [ "python","./main.py" ]