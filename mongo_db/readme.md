## mongodb

docker exec -it some-mongo bash
docker logs some-mongo
进入mongo客户端
docker exec -it python_docker_mongodb_1 mongo
进入bash
docker exec -it mongo_db_mongo_1 bash

mongodb的默认储存文件路径 /data/db

docker 命令运行，指定config文件
$ docker run --name some-mongo -v /my/custom:/etc/mongo -d mongo --config /etc/mongo/mongod.conf
