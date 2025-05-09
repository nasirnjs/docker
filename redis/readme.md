
Check Redis Stats (Memory, Clients, etc.)
```
docker exec -it redis-master redis-cli INFO memory
docker exec -it redis-master redis-cli INFO clients
docker exec -it redis-slave redis-cli INFO memory
docker exec -it redis-slave redis-cli INFO clients
```

You can also check replication info or general server info:

```
docker exec -it redis-master redis-cli INFO replication
docker exec -it redis-slave redis-cli INFO replication
```

Check Slow Log (for long-running queries)

```
docker exec -it redis-master redis-cli SLOWLOG GET
docker exec -it redis-slave redis-cli SLOWLOG GET
```

To check for any pending commands on the Redis instance (useful in high-traffic situations):

```
docker exec -it redis-master redis-cli CLIENT LIST
docker exec -it redis-slave redis-cli CLIENT LIST
```

