# redis dockerfile

一行命令:
docker run --name hupu_redis   -v /data/redis/data:/data -d redis -h redis  redis-server --appendonly yes
