# gitlab-runner

使用gitlab 私有runner docker镜像安装

指令
docker-compose run --rm gitlab-runner register -n \
  --url https://gitlab.com/ \
  --registration-token M5JN3aSybZ5HX39YvxaT \
  --executor docker \
  --description "icecola's Docker Runner" \
  --docker-image "docker:stable" \
  --docker-volumes /var/run/docker.sock:/var/run/docker.sock

运行: docker-compose up -d

在gitlab设置中指定tags
