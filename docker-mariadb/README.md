```bash
apt-get update
apt-get install -y mysql-client
```


`mysql -h 0.0.0.0 -P 3306 -u root -pPass4You`



 The --bind-address=0.0.0.0 option in the command section of the Docker Compose file overrides the default bind address configuration in the MariaDB container. This ensures that MariaDB listens on all available network interfaces, including the host's IP address, allowing connections from outside the container.

The custom.cnf file you're using to set bind-address = 0.0.0.0 is another way to achieve the same result. However, the Docker Compose option --bind-address=0.0.0.0 is more explicit and ensures that the bind address is correctly set even if the configuration file changes or is not loaded for some reason.