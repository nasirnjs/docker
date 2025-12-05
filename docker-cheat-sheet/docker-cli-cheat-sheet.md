# 🚀Docker Cheat Sheet/CLI Commands🚀

**Virtualization:** Each VM runs a full OS with its own kernel and drivers via a hypervisor (VMware, Hyper-V, KVM). Heavy but fully isolated; VMs take minutes to start.

**Containerization:** Containers share the host OS kernel, running isolated processes with their own filesystem. Lightweight and fast, starting in milliseconds. All containers must match the host kernel (e.g., Linux containers on Linux).


<!-- Centered image with width and height -->

<p align="center">
  <img src="image/vm-container.png" alt="Virtualization vs. Containerization" width="400" height="500">
</p>

<!-- Optional caption -->

<p align="center"><em>Figure 1: Virtualization vs. Containerization</em></p>




| Feature            | Virtualization (VMs)                                                            | Containerization (Docker, Podman)                                                                 |
| ------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Definition**     | Running multiple virtual machines on a single physical host using a hypervisor. | Running multiple containers sharing the same OS kernel on a single host using a container engine. |
| **Isolation**      | Full isolation with separate OS for each VM.                                    | Process-level isolation using namespaces and cgroups, sharing the host OS kernel.                 |
| **Resource Usage** | Heavy, because each VM includes a full OS.                                      | Lightweight, containers only include the application and dependencies.                            |
| **Startup Time**   | Slow, minutes to boot an OS.                                                    | Fast, seconds to start a container.                                                               |
| **Portability**    | VMs are less portable, depend on hypervisor compatibility.                      | Containers are highly portable: “Build once, run anywhere”.                                       |
| **Performance**    | Slightly lower, due to full OS overhead.                                        | Near-native performance, minimal overhead.                                                        |
| **Size**           | Large (GBs per VM)                                                              | Small (MBs per container)                                                                         |
| **Use Case**       | Running multiple OS types, legacy applications, full OS isolation.              | Microservices, CI/CD pipelines, cloud-native applications.                                        |
| **Management**     | Requires hypervisor management, OS updates, and patching per VM.                | Easier to manage, simpler to deploy and scale applications.                                       |


## Let’s try some basic command 

## 🚀 Basic Docker Commands Cheat Sheet 🚀

🔹 ## Basic Commands
```bash
docker version
docker info
docker ps
docker ps -a
docker images
docker pull nginx
docker system df
```

🔹 ## Run Containers
```bash
docker run nginx
docker run -d nginx
docker run -d --name web -p 8080:80 nginx
docker run -it ubuntu bash
```

🔹 ## Start / Stop / Restart
```bash
docker stop <id>
docker start <id>
docker restart <id>
docker kill <id>
```
🔹 ## Remove Containers / Images
```bash
docker rm <id>
docker rm -f <id>
docker rmi <image>
docker system prune
docker image prune -a
docker container prune
```

🔹 ## Logs / Exec / Inspect
```bash
docker logs <id>
docker exec -it <id> bash
docker inspect <id>
docker stats
docker top <id>
```
🔹 ## Copy Files
```bash
docker cp <id>:/path ./localpath
docker cp ./localpath <id>:/path
```

## Managing Docker Services and Sockets with Systemd

Docker service can still be activated through the Docker socket (`docker.socket`) even if you stop the Docker service (`docker.service`). The Docker socket allows communication with the Docker daemon and is used for Docker API access.

```bash
sudo systemctl status docker
sudo systemctl stop docker
sudo systemctl status docker
sudo systemctl stop docker.socket
```

---

## The lifecycle of a Docker container
The lifecycle of a Docker container involves creation, running, stopping, and removal. Containers are created from Docker images, run as isolated instances, can be stopped or paused, and can be removed when no longer needed.


<!-- Centered image with width and height -->

<p align="center">
  <img src="image/Container_life.png" alt="Lifecycle of Docker Container" width="700" height="400">
</p>

<!-- Optional caption -->

<p align="center"><em>Figure 1: Lifecycle of Docker Container</em></p>


**Example**

1. docker create:
Purpose: Creates a new container but does not start it.
Example: Creates a new container named "my-container" using the Nginx image but does not start it.
```
docker create --name my-container nginx
```

2. docker start:
Purpose: Starts one or more stopped containers.
Example: Starts the container named "my-container" that was previously created but stopped.
```
docker start my-container
```

3. docker run:
Purpose: Creates and starts a new container in a single command.
Example: This command combines the process of creating and starting a container named "my-container" using the Nginx image in a single step.
```
docker run --name my-container nginx
```

4. docker pause:
Purpose: Temporarily pause the processes in the running container. Example:
```bash
docker pause my-container
docker ps --filter "name=my-container"
docker unpause my-container
docker ps --filter "name=my-container"
```
5. docker stop:
Purpose: The docker stop command is used to stop a running container.Example: This command stop a container named "my-container".
```
docker stop my-container
```

6. docker rm:
Purpose: The docker rm command is used to remove a container.Example: Want to remove container named "my-container".
```
docker rm my-container
```

---

## Why a Docker container exits!!!
Docker containers are designed to run a specific command or process and exit when that command or process completes. The default behavior is to start the specified command or process inside the container and stop when that command or process finishes execution.
Docker containers run as long as the process inside the container is active.
Example: Default Shell Behavior (Container Stops Immediately).
Run a Command to Keep Container Running (e.g., Sleep). In the third example, the sleep 3600 command will keep the container running for 3600 seconds (1 hour), and then it will exit.
```
docker run busybox
docker run -it busybox
docker run busybox sleep 3600
```

---
🐳 ## Container Management

Run a container from an image.
```
docker ps
docker ps -a
docker exec my-nginx ls /usr/share/nginx/html
docker inspect my-nginx
docker stop my-nginx
docker container stop $(docker container ps -q)
docker start 24952546f818
docker restart 24952546f818
docker restart -t 30 6d144a1d546b
docker inspect --format='{{.Id}}' nginx
```

🐳 ## Build Docker Images

**What is a Docker Image?**
A Docker image is a read-only template that contains a set of instructions for creating a container that can run on the Docker platform.

**What is docker base image?**
A Docker base image is the initial image used as the foundation for building a Docker container.
It serves as the starting point from which your application and its dependencies are added to create a runnable environment.
Base images are typically pre-configured operating system images with certain tools, libraries, and settings already installed.

**Here's a basic Dockerfile for a Python "Hello, World!" application.**

```
vim app.py
```

```bash
from flask import Flask, Response
import requests
import datetime
import random

app = Flask(__name__)

@app.route('/<user>')
def hello_world(user):
    # Current server time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Call external API (GitHub)
    try:
        response = requests.get("https://api.github.com")
        api_status = response.status_code
    except:
        api_status = "Failed to reach API"
    
    # Funny messages
    funny_messages = [
        "Did you bring snacks? Because coding is hungry work! 🍕",
        "I tried to be normal once. Worst two minutes ever. 😎",
        "Keep calm and Docker on! 🐳",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
    ]
    
    random_funny = random.choice(funny_messages)
    
    # HTML content with improved styling
    html_content = f"""
    <html>
        <head>
            <title>Docker + Flask Fun</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f0f8ff;
                    padding-top: 50px;
                }}
                h1 {{
                    font-size: 60px;
                    font-weight: bold;
                    color: #333;
                }}
                p.funny {{
                    font-size: 28px;
                    font-weight: bold;
                    color: #0077cc;
                    margin-top: 20px;
                }}
                p.info {{
                    font-size: 22px;
                    color: #555;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <h1>Hello, {user}! 😁</h1>
            <p class="funny">{random_funny}</p>
            <p class="info">
                Server time: {current_time} <br>
                GitHub API status: {api_status}
            </p>
        </body>
    </html>
    """
    
    return Response(html_content, mimetype='text/html')

@app.route('/')
def default_user():
    return hello_world("Guest")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```
```
vim requirements.txt
```

```bash
flask
requests
#pandas
#beautifulsoup4
```

```bash
vim Dockerfile
```

```bash
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
```

🔹 ## Build & Tag Images

<img src="image/docker-image-tag.png" alt="Docker Image Taging explaination" width="800"/>

```bash
docker build -t myimage:1.0 .
docker tag myimage:1.0 repo/myimage:1.0
docker tag old-image:old-tag new-image:new-tag
```

## Authenticating to Registries
Docker and containerization, a registry is a service that stores and distributes Docker images. Docker images can be stored in public or private registries.
Here's an overview of public and private registries:

**Public Registry**
- Definition: Public storage service for Docker images, accessible to anyone.
- Example: Docker Hub (hub.docker.com).
- Use Cases: Sharing open-source or community-based images.
  
**Private Registry**
- Definition: Secure storage service for Docker images, requires authentication.
- Example: Self-hosted or third-party private registries.
- Use Cases: Storing proprietary or sensitive images, access control.

Log in to Docker Hub.
```
docker login
```

Check local Docker images list.
```
docker image list
```

Push Docker Image to Dockerhub Private Repo.
```
docker push nasirnjs:hello-python:001
```

Log in to a Private Registry.
```
docker login registry.example.com
```

Docker CLI configuration settings, including authentication credentials for Docker registries.
```
cat ~/.docker/config.json 
```

 Display information about disk usage related to Docker.
 ```
 docker system df
 ```


## Docker Image Layer
In Docker, images are composed of multiple layers. A docker container image is created using a dockerfile. Every line in a dockerfile will create a layer.
If you make changes to your Dockerfile and rebuild the image, Docker can reuse cached layers to speed up the process, only rebuilding the layers affected by the changes.  Caching plays a significant role in optimizing the build process.
Let's explore both concepts with examples:

```
### Docker Image Layers Explanation

1. **Base Image Layer**:
   - This layer is created when you specify `FROM python:3.8-slim`.
   - It pulls the official Python 3.8 slim image as the base for your image.

2. **Environment Variables Layer**:
   - This layer is created by `ENV PYTHONUNBUFFERED=1`.
   - It sets the `PYTHONUNBUFFERED` environment variable to `1`, ensuring that Python output is unbuffered and immediately printed to stdout.

3. **Working Directory Layer**:
   - This layer is created by `WORKDIR /app`.
   - It sets the working directory inside the container to `/app`.

4. **Copy Requirements Layer**:
   - This layer is created by `COPY requirements.txt /app/`.
   - It copies the `requirements.txt` file from your host machine into the `/app` directory within the container.

5. **Install Dependencies Layer**:
   - This layer is created by `RUN pip install --no-cache-dir -r requirements.txt`.
   - It installs the Python dependencies listed in `requirements.txt` using pip.
   - If the contents of `requirements.txt` haven't changed since the last build, Docker will reuse the cached layer for this step, improving build performance.

6. **Copy Application Code Layer**:
   - This layer is created by `COPY . /app`.
   - It copies the entire contents of your current directory (containing your application code) into the `/app` directory within the container.
   - If your application code hasn't changed since the last build, Docker will reuse the cached layer for this step, improving build performance.

7. **Expose Port Layer**:
   - This layer is created by `EXPOSE 8000`.
   - It exposes port 8000 on the container, allowing external access to the application running inside the container.

8. **Run Application Layer**:
   - This layer is created by `CMD ["python", "app.py"]`.
   - It specifies the default command to run when the container starts, which is to execute the `app.py` Python script using the Python interpreter.
   - This layer defines the entry point for your containerized application.

```

Build Docker Image form [Here](https://github.com/nasirnjs/docker-static-site)

list of `nginx` image layer.
```
docker image inspect nginx -f '{{.RootFS.Layers}}' | awk -F' ' '{for (i=1; i<=NF; i++) print $i}'
```

**Install Dive**
The dive is a command line tool for analyzing a Docker image. This tool shows image contents broken down by layer. It can used to explore image structure in order to minimize size of Docker image. [Reference](https://github.com/wagoodman/dive)

Install dive on Ubuntu
```
sudo snap install dive
```

Uninstall dive
```
sudo apt purge --autoremove -y dive
```


##  Difference between CMD vs ENTRYPOINT Docker!

In Docker, both `CMD` and `ENTRYPOINT` are instructions used to specify what command should be run when a container is started.
Y

**Docker CMD**
- Whenever we want to override executable while running the container, use `CMD`.
- We can override the value with a command-line argument.
- We can multiple CMD in a single docker file but only one will be executable while the container start.

**Docker ENTRYPOINT**
- ENTRYPOINT defines the fixed command the container will always run.
- ENTRYPOINT makes the container behave like an executable binary.
- If you pass arguments when running the container, they are appended to ENTRYPOINT unless you use the --entrypoint flag.

```bash
vim app.py
```
```bash
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World from Flask!</h1>"

if __name__ == '__main__':
    # Default port
    port = 5000

    # Look for --port argument
    if '--port' in sys.argv:
        try:
            i = sys.argv.index('--port')
            port = int(sys.argv[i + 1])
        except (IndexError, ValueError):
            print("Warning: Invalid or missing port, using 5000")
            port = 5000

    print(f"Starting Flask on http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port)
```

```
vim requirements.txt
```

```bash
Flask==2.3.3
```

```bash
Dockerfile
```
```bash
# Official slim Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose port (optional, just for documentation)
EXPOSE 5000

# This will ALWAYS run "python app.py"
ENTRYPOINT ["python", "app.py"]

# These are the DEFAULT arguments → can be overridden
CMD ["--port", "5000"]
```


Build Application
```bash
docker build -t myflask .
```
Runs on Default port 5000.
```bash
docker run -p 5000:5000 myflask
```
Override port to 8080
```bash
docker run -p 8080:8080 myflask --port 8080
```
```bash
docker run -p 3000:3000 myflask --port 3000
```

**Conclusion**
- Whenever there is a chance of overriding executable while running the container using CMD otherwise uses ENTRYPOINT.
- Sometimes we don’t have to override the executable all we want to run the container, in that case, ENTRYPOINT is the best use case.
- If ENTRYPOINT is used for the executable, we can use CMD to pass default parameters. In that case, we use both together.


## Don,t Ignore .dockerignore
The `.dockerignore` file is used by Docker to specify files and directories that should be excluded (ignored) when building a Docker image. It works similarly to the more widely known `.gitignore` file used by Git to specify files and directories that should be ignored when tracking changes.

Here's how it works:

- Default Behavior: By default, Docker includes all files and directories in the build context when building an image.
- Use of .dockerignore: If a file named .dockerignore is present in the build context, Docker reads it to determine which files and directories should be excluded from the build context.
- Exclusion Rules: The .dockerignore file follows the same rules as .gitignore. You can use wildcards and patterns to specify files and directories to be excluded.

For example, a .dockerignore file might look like this:
```
# .dockerignore
# Exclude the Dockerfile
Dockerfile
# Exclude the README.md file
README.md
# Exclude the .env file
.env
# Exclude the .git file
.git
```
Complete Example is [Here](https://github.com/nasirnjs/docker-static-site)

## Docker Args & Environment Variables

ARG and ENV are dockerfile instructions, which you can apply the different configurations.

ARG parameters are applied only during the docker image building process they are unavailable once you have built the image.
Default values can be specified for ARG parameters in the Dockerfile, and they can be modified during image creation.

You can pass ENV variables not only during the image building but also at runtime when your containers are running.
ENV can also have a default value in the dockerfile and you can override ENV values.

[Here](https://github.com/nasirnjs/docker-nodejs-env) is a Nodejs app ENV Example.


## Docker volume:

Docker volumes are used to persist data generated by and used by Docker containers. They provide a way to share data between containers and also to persist data even if the container is removed.

Here are some common Docker volume-related commands with examples:

List of Docker Volume.
```
docker volume ls
```

Create Docker volume.
```
docker volume create my_volume
```

List of Docker Volume.
```
docker volume ls
```

Inspect a Volume.
```
docker volume inspect my_volume
```

Remove a Volume.
```
docker volume rm my_volume
```

Create Nginx volume and run Nginx Pod with attached volume inside of Nginx Pod.
```bash
docker volume create web-data
docker run -d -p 8080:80 --name nginx-server -v web-data:/usr/share/nginx/html nginx
```
Login into container and update index.html and check data is persist, after update container data check host machine volume.
```bash
docker volume ls
docker inspect web-data
sudo su root
cd /var/snap/docker/common/var-lib-docker/volumes/web-data/_data
cat index.html
```

**Let's go through examples of anonymous volumes, named volumes, and bind mounts in Docker.**

1. Anonymous Volume:
Anonymous volumes are volumes without a specific name. They are created by Docker and associated with the container that uses them.
```bash
# Run Nginx container with an anonymous volume
docker run -d --name anonymous-nginx -v /usr/share/nginx/html nginx

# Check the volume details
docker inspect anonymous-nginx
```
In this example, the anonymous volume is automatically created for the default Nginx HTML path (/usr/share/nginx/html). It will be removed when the container is removed.

2. Named Volume:
Named volumes are explicitly created with a specific name, allowing for reusability and persistence.
```bash
docker volume create web-data
docker run -d -p 8080:80 --name nginx-server -v web-data:/usr/share/nginx/html nginx
```
Here, the named volume `web-data` is created, and it is mounted to the default Nginx HTML path `(/usr/share/nginx/html)` inside the named-nginx container.

3. Bind Mount:
Bind mounts allow you to mount a directory from the host machine into the container.
```
# Run a container with a bind mount
docker run -d -p 8080:80 --name bind-mount -v /home/nasir/bind-mount:/usr/share/nginx/html nginx

# Check the volume details
docker inspect bind-mount
```
In this case, the `/home/nasir/bind-mount` directory on the host machine is mounted into the default Nginx HTML path `(/usr/share/nginx/html)` inside the bind-nginx container. 


## Docker Namespace

Docker namespaces are a key feature of containerization that provide process isolation and resource abstraction, allowing multiple containers to run on the same host without interfering with each other. 

PID (Process ID) Namespace:
To check the PID (Process ID) Namespace of a running Docker container, you can use the docker inspect command.
Here's an example:
```
docker run -d --name=web nginx
docker inspect --format '{{.State.Pid}}' web
```
Network Namespace:
Let's use the example command you provided to check the PID and Network Namespace of the running Docker container.
```
docker inspect --format '{{.NetworkSettings.SandboxKey}}' web
```


## Docker Cgroups

Docker leverages several control groups (cgroups) controllers to manage and control resource usage within containers. Here are some common cgroups controllers used in Docker, along with examples:

CPU Controller:
Example: Limit a container to use a maximum of 50% of one CPU core.
```
docker stop my-container  && docker rm my-container
docker run -d --name my-container --cpus=0.5 nginx
docker inspect --format '{{.HostConfig.NanoCpus}}' my-container
```

Memory Controller:
Example: Restrict a container to use a maximum of 512 megabytes of memory.
```
docker stop my-container  && docker rm my-container
docker run -d --name my-container --memory=512m nginx
docker inspect --format '{{.HostConfig.Memory}}' my-container | numfmt --to=iec
```

Block I/O Controller:
Example: Control the maximum read and write rates to block devices for a container.
```
docker stop my-container  && docker rm my-container
docker run -d --name my-container --device-write-bps=/dev/sda:1mb nginx
docker inspect --format '{{.HostConfig.BlkioDeviceWriteBps}}' my-container | cut -d: -f2 | tr -d ']' | numfmt --to=iec
```

PIDs Controller:
Example: Limit the number of processes a container can create.
```
docker stop my-container  && docker rm my-container
docker run -d --name my-container --pids-limit=100 nginx
docker inspect --format '{{.HostConfig.PidsLimit}}' my-container
```

## Docker Networking

Docker networking facilitates communication between containers and the external environment through the host machine where the Docker daemon operates.

Docker comes with five built-in network drivers that implement core networking functionality. Network (bridge, host, ipvlan, macvlan, null & overlay)

**Here are examples and brief descriptions for each of the mentioned Docker network drivers.**

Check available network drivers from the "Plugins" section under "Server" vi `docker info` command.

**1. Bridge Driver Example:**
```bash
docker network create --driver=bridge my_bridge_net
docker run --network=my_bridge_net -d --name=web-server nginx
docker ps
docker inspect 454
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-server
```
*Description:*
- Default driver for container communication on a single host.
- Containers share the host's network stack by default.

**2. Host Driver Example:**
`docker run --network=host -d --name=web-server nginx`

*Description:*
- Containers use the host's network directly.
- No network isolation between containers.
- Bind them to the same host port 80.

**3. IPvlan Driver Example:**

```bash
docker network create -d ipvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o ipvlan_mode=l2 my_ipvlan_net
docker run --network=my_ipvlan_net -d --name=web-server nginx
docker ps
docker inspect 1f9
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-server
```
*Description:*
- Configures sub-interfaces with unique MAC and IP addresses.
- Containers can directly connect to the physical network.

**4. Macvlan Driver Example:**

```
docker network create -d macvlan --subnet=192.168.10.0/24 --gateway=192.168.10.1 -o parent=eno1 my_macvlan_network
docker run --network=my_macvlan_network -d --name=web-server nginx
docker ps
docker inspect 1022
docker inspect -f '{{.NetworkSettings.Networks.my_macvlan_network.IPAddress}} {{.NetworkSettings.Networks.my_macvlan_network.MacAddress}}' web-server
```

*Description:*
- Creates sub-interfaces with unique MAC and IP addresses.
- Containers appear as individual devices on the network.

**5. Null Driver Example:**

```
docker run --network=none -d --name=web-server nginx
docker ps
docker inspect 454
docker inspect -f '{{.NetworkSettings.Networks.none.IPAddress}} {{.NetworkSettings.Networks.null.MacAddress}}' web-server
```

*Description:*
- Provides an isolated environment where containers can't communicate.
- Useful for scenarios requiring complete network isolation.

**6. Overlay Driver Example:**

```
docker network create --driver=overlay my_overlay_network
docker service create --network=my_overlay_network my_service
```

*Description:*
- Enables multi-host networking in Docker Swarm.
- Uses overlay networks for communication across different hosts.


## Building Multi Container Application with Docker



## Container Cleanup:
docker container prune: Remove all stopped containers.
docker container stop $(docker container ps -q): Stop all running containers.
docker container rm $(docker ps -aq): Remove all containers.




## Docker Restart Policy:



[Ref](https://docs.docker.com/engine/reference/run/)