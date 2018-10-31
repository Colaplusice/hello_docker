## hello_docker

学习docker的仓库

## 基于docker的wordpress
- docker-compose up -d
- docker compose down --vlolumes 删除所有内容
- docker compose down 不删除数据库

本机挂载目录到docker:
docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py
加载主机的/src/webapp 目录到容器的/opt/webapp目录。

## 网络

-P 随机端口映射
-p 5000:5000 选定端口映射

## 容器交互

数据库容器 docker run -d --name db training/postgres
web容器 docker run -d -P --name web --link db:db traing/webapp python app.py
可以避免数据库端口的映射
可以使用env命令查看web容器的环境变量
或者通过父容器的/etc/hosts文件
父容器即是link左边的容器，比如web容器
可以通过ping测试链接的容器 ping db
可以链接多个父容器到子容器上

### docker网络原理

docker启动是会创建一个docker0的网桥，随机分配一个私有网络段到docker0，比如172.17.42.1 掩码为255.255.0.0。以后启动的所有容器的网口会获得一个子网地址。
同时会创建一对veth pair接口，接口的一端在容器中，一端在网桥上。也就是说，主机--->网桥--->vethpair--->容器，进行通讯
网络的高级配置

- -b bridge or --bridge=BRIDGE 指定挂载的网桥
- --bip=CIDR 定义子网掩码
- -H socket docker服务端接收命令的通道
- --icc=true|false 是否支持容器间通信
- --ip-forward=true|false 
- --iptables=true|false 是否可以添加iptables规则
- --mtu=BYTES --容器网络中的mtu
- --dns =IP_ADDRESS 指定dns服务器
- --dns-search=DOMAIN 指定dns搜索域

## dockerfile

from
指定源镜像
MAINTAINER
维护者
RUN
run <command> 在shell终端中执行，即bin/sh  run ["","param1","param2"] 这个可以在其他终端执行，每条run语句都会在当前基础镜像上生效。

CMD["executable","param1","param2"] 使用exec执行，每个dockerfile只会有一条cmd命令

EXPOSE 暴露端口

ENV 环境变量

ADD <src> <des> src是dockerfile的相对路径，也可以是url，也可以是tar文件

ENTRYPOINT
配置容器启动后执行的命令，而且不能被docker run 提供的参数覆盖
只能有一个endpoint

VOLUME
VOLUME["/data"]创建一个本地的挂载点，一般用来存放数据库数据，应该是dockerfile的相对路径

USER 运行容器时的用户名

WORKDIR 为后续的RUN,CMD,ENTRYPOINT指定工作路径  可以叠加指定，
WORKDIR /a
WORKDIR b
WORKDIR c
最终的路径为a/b/c

ONBUILD 配置当前创建的镜像作为其他新建镜像的基础镜像

容器的原理
利用Linux命名空间作为权限的隔离控制，利用cgroups来做资源分配

## docker-compose

命令
docker-compose <command> 
build 构建服务
help  获得帮助
kill 停止容器
logs 查看日志
port 打印端口
ps  列出容器
pull 拉取镜像
rm 删除容器
run 在服务上执行命令    $ docker-compose run ubuntu ping docker.com
scale 指定运行的容器个数
start 启动已经存在的容器
stop 停止容器
docker-compose up -d 会在后台启动并创建所有的容器

## docker-compose yaml模板
image: 镜像
build 指定dockerfile的路径  build: /path/to/build/dir
command 启动后默认执行的命令
links 链接到其他容器
external_links 链接到docker-compose外的容器
ports 端口信息
expose 内部端口暴露
volumes 挂载路径设置
volumes_from 从另一个容器或者服务挂载
environment 环境变量
environment:
RACK_ENV: development
SESSION_SECRET:
environment:

- RACK_ENV=development
- SESSION_SECRET

env_file 从文件中读取环境变量
extends 基于已有的服务进行扩展
extends:
    file: common.yml
    service: webapp
相当于继承



