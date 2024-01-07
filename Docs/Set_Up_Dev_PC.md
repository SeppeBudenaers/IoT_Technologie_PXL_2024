# Set Up Dev PC

## Setting up SSH

* Generating SSH key to safely log in to IoT device. 

In order to use SSH on a computer a few tools will be needed:
  * An ssh key in order to login to it.
  * Tailscale: A safe vpn that will allow us to keep the Pi in one safe space and also access it remotely.
  * A raspberry Pi setup with the needed [tools](Docs/Set_Up_Pi.md).
 
    
## SSH into a raspberry Pi

Firstly the raspberry Pi must be setup for SSH this can be found inside the [documentation for the pi](Docs/Set_Up_Pi.md), if this is done you will have an IP adress to login to with SSH.

## Tailscale:

In order to setup tailscale you will need a tailscale account and a github account it is important to link these accounts. Then you can go to [Tailscale](https://tailscale.com/download/windows) and download it. Once the installation is complete you will need to add your PC or laptop to the list of devices. This can be done by opening Tailscale and following the steps the installer will give you. Once this is complete the admin console can be accessed, and if you or your team needs to access the Pi remotely. If the Pi is yours this should already have happend with the steps above but for your team members you will need to create an invite to add the device.

```
curl -fsSL https://tailscale.com/install.sh | sh
````
## Setting up Docker

* Creating a Docker hub account 

* Generating Docker token (this will be used to upload your docker image from github to dockerhub)

## Github

* Cloning this repository 

* Adding github secrets 

## Running the github action
