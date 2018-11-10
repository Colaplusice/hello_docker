# nginx

nginx 有两个配置文件，一个是默认的初始化文件，在/etc/nginx/conf.d/default.conf
还有一个在 /etc/nginx/nginx.conf    这个是用户可以手动配置的，同时conf.d/下的文件都被引入到了这里来。  我们在conf.d下再加一个文件，flag.conf
命令行运行+配置文件挂载+端口映射

挂载html文件夹和nginx.conf文件   需要正确的nginx.conf配置文件才能运行起来 ro read only, html路径下必须有一个index.html作为显示的页面
$ docker run --name base-nginx -p 8080:80 -v /Users/icecola/Desktop/hello_docker/nginx/conf.d:/etc/nginx/conf.d:ro -v /Users/icecola/Desktop/hello_docker/nginx/html:/usr/share/nginx/html:ro -d nginx

运行后应该在本机8080端口看到 hello docker and nginx的字样

## dockerfile运行

打镜像
docker build . -t nginx/docker_nginx

name在build的时候指定

## docker-compose 运行

docker-compose up -d 即可
docker-compose down  停掉

## 架设国旗服务器

docker run --name base-nginx -p 8001:8001 -p 8080:80  -v /Users/icecola/Desktop/hello_docker/nginx/conf.d:/etc/nginx/conf.d:ro -v /Users/icecola/Desktop/hello_docker/nginx/country_flag/countries/:/home/countries/ -v /Users/icecola/Desktop/hello_docker/nginx/html:/usr/share/nginx/html:ro  -v /Users/icecola/Desktop/hello_docker/nginx/logs:/var/log/nginx -d nginx

发现无法定位到Log  指定Log file

nginx log level

emerg: Emergency situations where the system is in an unusable state.
alert: Severe situation where action is needed promptly.
crit: Important problems that need to be addressed.
error: An Error has occurred. Something was unsuccessful.
warn: Something out of the ordinary happened, but not a cause for concern.
notice: Something normal, but worth noting has happened.
info: An informational message that might be nice to know.
debug: Debugging information that can be useful to pinpoint where a problem is occurring.

## 设置Log 文件大小

在 /etc/logrotate.d/nginx 指定大小
```
/var/log/nginx/access_log {
    rotate 7
    size 5k
    dateext
    dateformat -%Y-%m-%d
    missingok
    compress
    sharedscripts
    postrotate
        test -r /var/run/nginx.pid && kill -USR1 `cat /var/run/nginx.pid`
    endscript
}
```