#!/bin/bash

dockerTag="latest"

Help()
{
   # Display Help
   echo "These are the functions in this script"
   echo
   echo "Syntax: scriptTemplate [-h|t|p|r]"
   echo "options:"
   echo "h     Print this Help."
   echo "t     Enter a tag for the monsterseppe/iot: docker."
   echo "p     Pull the docker."
   echo "r     Run the docker."
   echo
}

PullDocker() {
    echo "Pulling docker monsterseppe/iot:$dockerTag"
    docker pull monsterseppe/iot:$dockerTag
}

RunDocker() {
    echo "Running docker monsterseppe/iot:$dockerTag"
    docker run --privileged --device=/dev/spidev0.0:/dev/spidev0.0 monsterseppe/iot:$dockerTag
}

while getopts ":ht:p" option; do
    case $option in
        h) # Display Help
            Help
            exit;;
        t) # Option with argument
            dockerTag="$OPTARG"
            ;;
        p) # PullDocker
            PullDocker
            exit;;
        r) #RunDocker
            RunDocker
            exit;;
        \?) # Invalid option
            echo "Error: Invalid option"
            exit;;
    esac
done

