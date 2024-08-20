Steps 1: Copy env.example to .env

Steps 2: To run MySQL and PhpMyadmin at a time use `docker compose up -d --build`

Steps 3: To down `docker compose down`

Steps 4: If you want to run specific service run specific service name, example "docker compose up -d phpmyadmin"
---


You can log in to the MySQL container and access the MySQL shell directly in a single command

`docker exec -it my-mysql mysql -u root -p`


