# Set Up Pi

## SSH

### logging into Pi via SSH



### generating keys 



### authorizing Dev PC key 



### SSH login only



## SPI

### enabling spi 



## Docker

### installing docker 



### logging into docker 



### dockerscript to pull and run the IoT application



## Auto update 

### creating bash script to automatically update

```bash
sudo bash -c 'echo -e "#!/bin/bash\n\ndockerTag=\"latest\"\nbDockerrun=0\nHelp()\n{\n   # Display Help\n   echo \"These are the functions in this script\"\n   echo\n   echo \"Syntax: scriptTemplate [-h|t|p|r]\"\n   echo \"options:\"\n   echo \"h     Print this Help.\"\n   echo \"t     Enter a tag for the monsterseppe/iot: docker.\"\n   echo \"p     Pull the docker.\"\n   echo \"r     Run the docker.\"\n   echo \"u     Update the docker\"\n   echo\n}\n\nPullDocker() {\n    echo \"Pulling docker monsterseppe/iot:\$dockerTag\"\n    docker pull monsterseppe/iot:\$dockerTag\n}\n\nCheckContainerID(){\ncontainer_id=\$(docker ps --filter \"ancestor=monsterseppe/iot:\$dockerTag\" --format \"{{.ID}}\")\n}\n\nStopDocker(){\n    if [ -n \"\$container_id\" ]; then\n        echo \"stopping container with id: \$container_id\"\n        docker stop \$container_id\n    fi\n}\n\nUpdateDocker(){\n    PullDocker\n    CheckContainerID\n    StopDocker\n}\n\nwhile getopts \":ht:pru\" option; do\n    case \$option in\n        h) # Display Help\n            Help\n            exit;;\n        t) # Option with argument\n            dockerTag=\"\$OPTARG\"\n            ;;\n        p) # PullDocker\n            PullDocker\n            ;;\n        u) #UpdateDocker\n            UpdateDocker\n            bDockerrun=1\n            ;;\n        r) #RunDocker\n            bDockerrun=1\n            ;;\n        \\?) # Invalid option\n            echo \"Error: Invalid option\"\n            exit;;\n    esac\n\ndone\n\nif [ \$bDockerrun = 1 ]; then\n    echo \"Running docker monsterseppe/iot:\$dockerTag\"\n    docker run -d --privileged --device=/dev/spidev0.0:/dev/spidev0.0 monsterseppe/iot:\$dockerTag\nfi\n" > /usr/local/bin/dockerscript.sh && chmod +x /usr/local/bin/dockerscript.sh'
```
#### OR
```cmd
sudo touch /usr/local/bin/dockerscript.sh
sudo nano /usr/local/bin/dockerscript.sh
```
#### copy and past this into dockerscript.sh
```bash
#!/bin/bash

dockerTag="latest"
bDockerrun=0
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
   echo "u     Update the docker"
   echo
}

PullDocker() {
    echo "Pulling docker monsterseppe/iot:$dockerTag"
    docker pull monsterseppe/iot:$dockerTag
}

CheckContainerID(){
container_id=$(docker ps --filter "ancestor=monsterseppe/iot:$dockerTag" --format "{{.ID}}")
}

StopDocker(){
    if [ -n "$container_id" ]; then
        echo "stopping container with id: $container_id"
        docker stop $container_id
    fi
}

UpdateDocker(){
    PullDocker
    CheckContainerID
    StopDocker
}

while getopts ":ht:pru" option; do
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
        u) #UpdateDocker
            UpdateDocker
            bDockerrun=1
            ;;
        r) #RunDocker
            bDockerrun=1
            ;;
        \?) # Invalid option
            echo "Error: Invalid option"
            exit;;
    esac
done

if [ $bDockerrun = 1 ]; then
    echo "Running docker monsterseppe/iot:$dockerTag"
    docker run -d --privileged --device=/dev/spidev0.0:/dev/spidev0.0 monsterseppe/iot:$dockerTag
fi
```

### creating a `systemd` service
```cmd
sudo bash -c 'echo -e "[Unit]\nDescription=Script to pull docker IOT\nAfter=network-online.target\nWants=network-online.target\n\n[Service]\nExecStart=/usr/local/bin/dockerscript.sh -u -t latest\n\n[Install]\nWantedBy=default.target\n" > /etc/systemd/system/docker-update.service && nano /etc/systemd/system/docker-update.service'
```
#### or
```cmd
sudo touch /etc/systemd/system/docker-update.service
sudo nano /etc/systemd/system/docker-update.service
```
#### copy and past this into docker-update.service
```bash
[Unit]
Description=Script to pull docker IOT
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/local/bin/dockerscript.sh -u -t latest

[Install]
WantedBy=default.target
```

### creating a `systemd` timer
```cmd
sudo touch /etc/systemd/system/docker-update.timer
sudo nano /etc/systemd/system/docker-update.timer
```
#### copy and past this into docker-update.timer
```bash
[Unit]
Description=Run docker-update.service 2min after boot and 15 minutes

[Timer]
OnBootSec=2min
OnCalendar=*:0/15
Persistent=true

[Install]
WantedBy=timers.target
```

### enabling timer
```cmd
sudo systemctl daemon-reload
sudo systemctl enable docker-update.timer
sudo systemctl start docker-update.timer
```