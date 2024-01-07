# Set Up Pi

## Installing Pi OS



## SSH

* Logging into Pi via SSH



* Generating keys 



* Authorizing Dev PC key 



* SSH login only



* SPI


* Enabling spi 



## Docker

* Installing docker 



* Logging into docker 



* Dockerscript to pull and run the IoT application



## Auto update 

* Creating bash script to automatically update (option number one)

```bash
sudo bash -c 'echo -e "#!/bin/bash\n\ndockerTag=\"latest\"\nbDockerrun=0\nHelp()\n{\n   # Display Help\n   echo \"These are the functions in this script\"\n   echo\n   echo \"Syntax: scriptTemplate [-h|t|p|r]\"\n   echo \"options:\"\n   echo \"h     Print this Help.\"\n   echo \"t     Enter a tag for the monsterseppe/iot: docker.\"\n   echo \"p     Pull the docker.\"\n   echo \"r     Run the docker.\"\n   echo \"u     Update the docker\"\n   echo\n}\n\nPullDocker() {\n    echo \"Pulling docker monsterseppe/iot:\$dockerTag\"\n    docker pull monsterseppe/iot:\$dockerTag\n}\n\nCheckContainerID(){\ncontainer_id=\$(docker ps --filter \"ancestor=monsterseppe/iot:\$dockerTag\" --format \"{{.ID}}\")\n}\n\nStopDocker(){\n    if [ -n \"\$container_id\" ]; then\n        echo \"stopping container with id: \$container_id\"\n        docker stop \$container_id\n    fi\n}\n\nUpdateDocker(){\n    PullDocker\n    CheckContainerID\n    StopDocker\n}\n\nwhile getopts \":ht:pru\" option; do\n    case \$option in\n        h) # Display Help\n            Help\n            exit;;\n        t) # Option with argument\n            dockerTag=\"\$OPTARG\"\n            ;;\n        p) # PullDocker\n            PullDocker\n            ;;\n        u) #UpdateDocker\n            UpdateDocker\n            bDockerrun=1\n            ;;\n        r) #RunDocker\n            bDockerrun=1\n            ;;\n        \\?) # Invalid option\n            echo \"Error: Invalid option\"\n            exit;;\n    esac\n\ndone\n\nif [ \$bDockerrun = 1 ]; then\n    echo \"Running docker monsterseppe/iot:\$dockerTag\"\n    docker run -d --privileged --device=/dev/spidev0.0:/dev/spidev0.0 monsterseppe/iot:\$dockerTag\nfi\n" > /usr/local/bin/dockerscript.sh && chmod +x /usr/local/bin/dockerscript.sh'
```
* Alternatively
```cmd
sudo touch /usr/local/bin/dockerscript.sh
sudo nano /usr/local/bin/dockerscript.sh
```
* Copy and past this into dockerscript.sh

[dockerscript](App/DockerScript.sh)


* Creating a `systemd` service
```cmd
sudo bash -c 'echo -e "[Unit]\nDescription=Script to pull docker IOT\nAfter=network-online.target\nWants=network-online.target\n\n[Service]\nExecStart=/usr/local/bin/dockerscript.sh -u -t latest\n\n[Install]\nWantedBy=default.target\n" > /etc/systemd/system/docker-update.service'
```
* or
```cmd
sudo touch /etc/systemd/system/docker-update.service
sudo nano /etc/systemd/system/docker-update.service
```
* Copy and past this into docker-update.service
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

* Creating a `systemd` timer
```cmd
sudo bash -c 'echo -e "[Unit]\nDescription=Run docker-update.service 2min after boot and 15 minutes\n\n[Timer]\nOnBootSec=2min\nOnCalendar=*:0/15\nPersistent=true\n\n[Install]\nWantedBy=timers.target\n" > /etc/systemd/system/docker-update.timer'
```
* Alternatively
```cmd
sudo touch /etc/systemd/system/docker-update.timer
sudo nano /etc/systemd/system/docker-update.timer
```
* Copy and past this into docker-update.timer
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

### Enabling timer
```cmd
sudo systemctl daemon-reload
sudo systemctl enable docker-update.timer
sudo systemctl start docker-update.timer
```
