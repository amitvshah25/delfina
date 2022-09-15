# delfina project

### Start Web Project
- `docker-compose up --build`
- Open browser with [this URL](http://localhost:8080/picture) to see random dolphin image

### Run tests
`docker exec -it amit-delfina-web pytest`

#### Main libraries used in the project - 
- fastapi
- uvicorn
- slowapi (to ratelimit)
- requests
