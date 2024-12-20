docker pull redis
docker run -it --rm --name redis -p 6378:6379 redis
docker exec -it redis sh