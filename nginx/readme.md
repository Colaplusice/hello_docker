## nginx

命令行运行+配置文件挂载+端口

挂载html文件夹和nginx.conf文件   需要正确的nginx.conf配置文件才能运行起来 ro read only, html路径下必须有一个index.html作为显示的页面
$ docker run --name base-nginx -p 8080:80 -v /Users/icecola/Desktop/hello_docker/nginx/nginx.conf:/etc/nginx/nginx.conf:ro -v /Users/icecola/Desktop/hello_docker/nginx/html:/usr/share/nginx/html:ro -d nginx

只挂载html文件夹(nginx可以正常运行)
docker run --name base-nginx -p 8080:80 -v /Users/icecola/Desktop/hello_docker/ngi
nx/html:/usr/share/nginx/html:ro -d nginx

## dockerfile运行

打镜像
docker build . -t nginx/docker_nginx

name在build的时候指定

## docker-compose 运行

docker-compose up -d 即可
docker-compose down  停掉
