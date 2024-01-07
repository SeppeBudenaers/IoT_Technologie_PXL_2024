# Total grade: 11/20
## Git 0/7
- [ ] **The group is capable of showing they worked as a unit, and not as individuals**
- [ ] The group has good automation hygiene (no manual tasks, plenty of automation, …)
- [ ] The group has good Git hygiene (commit messages, branching, consistency, …)
- [ ] The group has good GitHub hygiene (pull requests, issues, actions, …)
- [ ] **The group produced** [**good documentation**](https://documentation.divio.com/) **about the project**
- [ ] The group was capable of creating a good developer experience (getting started in the README)
- [ ] **The group is capable of explaining what makes their project an IoT project**


## IOT Setup 4/6
- [x] **An IoT device is connected to the internet**
- [ ] More than one IoT device are connected to each other (mesh)
- [x] **An IoT device is securely connected to the internet**
- [X] **An IoT device of which the application software automatically updates itself (OTA)**
- [ ] An IoT device can be completely updated over the air (kernel upgrade)*
- [x] An IoT device is capable of being serviced remotely


## Application 3/7
- [x] **The application software is capable of speaking to an HTTPS CRUD endpoint**
- [X] **The application software is well written (clean code)**
- [ ] The application software uses Xilinx SDK code*
- [ ] The application software is written in a consistent style
- [ ] There is automation to lint the application software
- [x] **The application software is automatically built**
- [x] **The application software is automatically packaged**


## Extra  3/7
- [x] The application software is packaged in either a [Docker](https://www.docker.com/) format, or a [DEB format](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html)
- [ ] The application software is packaged in [Nix](https://nixos.org/)
- [ ] The IoT device is capable of being monitored (node_exporter)
- [ ] The application software uses Python and uses [Poetry](https://python-poetry.org/) as a dependency manager
- [x] The IoT device drives external hardware
- [X] A Linux kernel module drives the external hardware*
- [ ] The HTTPS CRUD endpoint is self-hosted (AWS, Azure, on-premise, …)

## Things I feel deserve extra points 1/1
- [x] added a feature writen in golang to the [CRUD endpoint](https://github.com/bryanhonof/iot-api-server/pull/1)
