#!/bin/sh

docker pull --platform linux/amd64 mysql:8.0
docker run -d -p 3307:3306 --name fastapi-mysql -e MYSQL_ROOT_PASSWORD=1234 \
  mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
