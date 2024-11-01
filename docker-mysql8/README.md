Steps 1: Copy env.example to .env

Steps 2: To run MySQL and PhpMyadmin at a time use `docker compose up -d --build`

Steps 3: To down `docker compose down`

Steps 4: If you want to run specific service run specific service name, example "docker compose up -d phpmyadmin"

---


You can log in to the MySQL container and access the MySQL shell directly in a single command

`docker exec -it my-mysql mysql -u root -p`



***MySQL Connection Timeout and Maximum Connections Setting*

```bash
    volumes:
      - mysql-data:/var/lib/mysql
      - ./init-db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
      - ./my.cnf:/etc/mysql/conf.d/my.cnf
```

`vim my.cnf`

```bash
[mysqld]
#This variable defines the time (in seconds) that the server waits for activity on a non-interactive connection before closing it.
wait_timeout = 300;

#Similar to wait_timeout, but it applies to interactive connections (such as those made using the MySQL client).
interactive_timeout = 300;

#This sets the maximum number of simultaneous client connections allowed to the MySQL server
max_connections=300
```


This command allows you to run a command in a running container.\
`docker exec -it my-mysql mysql -u root -pOf0cVeg`


This command displays a list of currently running threads (processes) in the MySQL serve.\
`SHOW PROCESSLIST;





