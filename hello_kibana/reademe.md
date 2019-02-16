# elasticsearch和kibana

## elastisearch

后台启动启动es

brew services start elasticsearch
启动   elasticsearch
elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml

elasticsearch.yaml默认的地址: /usr/local/etc/elasticsearch/elasticsearch.yaml

启动kibana kibana

端口 9200
url: http://elasticsearch:9200
kibana的地址:
 
 http://localhost:5601

## docker 安装kibana

docker pull docker.elastic.co/kibana/kibana:6.5.1

$ docker run -d --name kibana --net somenetwork -p 5601:5601 kibana:tag
端口隐射为5601


## docker-compose 

version: '2'
services:
  kibana:
    image: docker.elastic.co/kibana/kibana:6.5.1
    volumes:
      - ./kibana.yml:/usr/share/kibana/config/kibana.yml

通过环境变量配置
version: '2'
services:
  kibana:
    image: docker.elastic.co/kibana/kibana:6.5.1
    environment:
      SERVER_NAME: kibana.example.org
      ELASTICSEARCH_URL: http://elasticsearch.example.org


default 配置
server.name kibana
server.host 0
elasticsearch.url  http://elasticsearch:9200
xpack.monitoring.ui.container.elasticsearch.enabled true



brew install kibana

## 学习es

curl -XPUT http://127.0.0.1:9200/test

scoller
