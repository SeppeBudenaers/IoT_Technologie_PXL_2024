#!/bin/bash

dockerTag="latest"

Help() {
    echo "Sorry, I cannot help."
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
            ;;
        \?) # Invalid option
            echo "Error: Invalid option"
            exit;;
    esac
done

RunDocker
