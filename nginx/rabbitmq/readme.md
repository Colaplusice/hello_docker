# rabbitmq

web界面映射到 本地 8082端口
$ docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=newpass -p 8082:15672 rabbitmq:3-management

