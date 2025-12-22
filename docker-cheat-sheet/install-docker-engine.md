
# 🚀How To Install and Use Docker on Ubuntu 24.04🚀


## Install Docker Using the Official Convenience Script
Install Docker
```bash
curl -fsSL https://get.docker.com | sh
```

## Install Docker Engine on Ubuntu 24.04Lts [Reference](https://docs.docker.com/engine/install/ubuntu/)

**Install using the apt repository**

1. Set up Docker's apt repository.
   
```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```

2. Install the Docker packages.

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

1. Verify that the Docker Engine installation is successful by running the hello-world image.

```bash
sudo docker run hello-world
```

**Manage Docker as a non-root user**

The Docker daemon binds to a Unix socket, not a TCP port. By default it's the root user that owns the Unix socket, and other users can only access it using sudo. The Docker daemon always runs as the root user.\
If you don't want to preface the docker command with sudo add user to docker group.

1. Add your user to the docker group.

```bash
sudo usermod -aG docker $USER
```

2. Starts a new shell with the updated group memberships without requiring a logout.

```bash
newgrp docker
```

**Configure Docker to start on boot with systemd and disable**

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

sudo systemctl disable docker.service
sudo systemctl disable containerd.service
```
---
## Uninstall Docker Engine

1. Uninstall the Docker Engine, CLI, containerd, and Docker Compose packages

```bash
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
```

2. Images, containers, volumes, or custom configuration files on your host aren't automatically removed. To delete all images, containers, and volumes.

```bash
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

🎉🎉🎉 Congratulations!!! 🎉🎉🎉
