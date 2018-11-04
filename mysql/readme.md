## mysql 

docker run -d --name mysql -v ~/data/mysql/data:/var/lib/mysql -v ~/data/mysql/log:/var/log/mysql -v /Users/icecola/Desktop/hello_docker/mysql/conf:/etc/mysql/conf.d --log-opt max-size=10m -p 3306:3306 --log-opt max-file=9 -e MYSQL_ROOT_PASSWORD=newpass mysql:5.6 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

<!-- -e 指定screct文件 -e MYSQL_ROOT_PASSWORD_FILE=/run/secrets/mysql-root-->