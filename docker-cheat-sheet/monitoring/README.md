Make monitoring directory and keep scrape and stack both both file in same directory. 

```bash
└── monitoring
    ├── prometheus-scrape.yaml
    ├── prometheus-stack.yaml
    └── README.md
```
**Before apply update IP of your Cluster in scrape.yaml file**

First create a network.
```bash
docker network create --driver=overlay monitoring
```

Then run Stack.
```bash
docker stack deploy -c prometheus-stack.yaml promethous
```

To update specific Server.
```bash
docker service update --force promethous_grafana
```

CPU uses query
```bash
100 - (avg(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```
Memory Query
```bash
(node_memory_MemTotal_bytes - node_memory_MemFree_bytes - node_memory_Buffers_bytes - node_memory_Cached_bytes) / node_memory_MemTotal_bytes * 100
```
Network Query
```bash
irate(node_network_receive_bytes_total[5m])
```

Cadvisor exporter
```bash
14282
```
Node Exporter
```bash
1860,9894
```