# Load Balancer Playground

#### Stack
- Docker compose
- Nginx
- Python

### terminal 1
```bash
docker compose up
```

### terminal 2
```bash
./traffic.sh | sort | uniq -c
```

### in order to change nginx balancing strategies see comments in nginx.conf, then
```bash
docker exec nginx-proxy nginx -s reload
```