

# Traditinal Deployment


## Step 1: Install MySQL 8 Database and Database and User for backend app


```bash
CREATE DATABASE studentdb;
CREATE USER 'student_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Nasir#4321';
GRANT ALL PRIVILEGES ON studentdb.* TO 'student_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## Step 2: Install OpenJDK 18 or Higher

Install OpenJDK 18 or Heigher, yoyu can follow this [steps](https://github.com/nasirnjs/LinuxOpsHub/blob/main/install-OpenJDK.md)

## Step 3: Install Maven

Download the Maven Binaries [from here](https://dlcdn.apache.org/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.tar.gz)

```bash
wget https://dlcdn.apache.org/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.tar.gz
 tar -xvf apache-maven-3.9.9-bin.tar.gz
 mv apache-maven-3.9.9 /opt
 sudo mv apache-maven-3.9.9 /opt
 M2_HOME='/opt/apache-maven-3.9.9/'
 PATH="$M2_HOME/bin:$PATH"
```
**Note:** I am using zshell if you are using bash use `vim ~/.bashrc`

`vim ~/.zshrc`

Add the following lines to the end of the file make permanent environment variables:

```bash
export M2_HOME='/opt/apache-maven-3.9.9'
export PATH="$M2_HOME/bin:$PATH"
```

`mvn -v` 

`java --version`


## Step 4: Build the Backend Application

God to backend project directory and run `mvn clean install -DskipTests`

after making .jar file move your jar file to  "mv student-0.0.1-SNAPSHOT.jar /var/www/html"


## Step 5: Create Systemd Service for backend app

Create Systemd Service you can [follow](https://github.com/nasirnjs/LinuxOpsHub/blob/main/create_systemd_service.md)

**Note** Make sure your JDK and Maven path `which java` `which mvn` for systemd service.

`sudo vim /etc/systemd/system/lendingapp.service`

```bash
[Unit]
Description=Lending Application

[Service]
Type=simple
Restart=always
User=root
Group=www-data

# Define the log files
StandardOutput=append:/var/log/lendingapp.service.log
StandardError=append:/var/log/lendingapp.service.error.log

# Project root path
WorkingDirectory=/var/www/html/

# Command to execute the JAR file
ExecStart=/usr/local/jdk-18/bin/java -jar /var/www/html/student-0.0.1-SNAPSHOT.jar

[Install]
WantedBy=multi-user.target

```

`sudo systemctl daemon-reload`

`sudo systemctl enable lendingapp.service`

`sudo systemctl start lendingapp.service`

`sudo systemctl status lendingapp.service`


## Step 6: Run and Build Frontend

Install Node Version you can follow this [stesps](https://github.com/nasirnjs/LinuxOpsHub/blob/main/install-node-via-nvode-versionmanager.md#installing-node-using-the-node-version-manager) and Install Angular CLI globally.

Installing Node Using the Node Version Manager from [Here](https://github.com/nasirnjs/LinuxOpsHub/blob/main/install-node-via-nvode-versionmanager.md)

`npm i`

`npm run build`

`node --version`

`sudo npm install -g @angular/cli`

Navigate to your frontend project directory and run the following commands:

`npm install`

`npm run build`



## Step 7: Move the Dist Directory to Your Nginx Web Server Root Directory

```bash
sudo mv dist /var/www/html
ystemctl restart nginx.service
```

