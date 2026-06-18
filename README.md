# Load Balancer Playground

#### Stack
- Nx monorepo
- Docker compose
- Nginx
- Python / FastAPI
- Node.js / NestJS

#### Apps
- `apps/python`: existing stateless FastAPI application
- `apps/node`: stateless NestJS application with matching routes

### install Node workspace dependencies
```bash
npm install
```

### run apps with Nx
```bash
npm run start:python
npm run start:node
```

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
