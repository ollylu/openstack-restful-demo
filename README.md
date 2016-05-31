# 1、项目框架

![](http://o6p181fdf.bkt.clouddn.com/16-5-27/18951712.jpg)


# 2、项目目录结构


```
├── README.md                 (说明文档)
├── etc                       (配置文件目录)
│   ├── development.conf      (数据库配置等)
│   ├── logging_config.json   (日志配置文件)
│   └── paste_config.ini      (Paste配置文件)
├── apidoc                    (API接口文档)
│   ├── css /...
│   ├── img /...
│   ├── locales /...
│   ├── utils /...
│   ├── vendor /...
│   ├── api_project.json      (apidoc项目配置文件)
│   ├── ...
│   └── index.html
├── openstack                 (项目源码目录)
│   ├── auth                  (授权请求API)
│   │   ├── __init__.py
│   │   └── api.py
│   ├── common                (公用模块)
│   │   ├── __init__.py
│   │   ├── controllers.py
│   │   └── exceptions.py     (自定义异常)
│   ├── db                    (数据库相关模块)
│   │   ├── __init__.py
│   │   ├── api.py            (数据库API)
│   │   └── models.py         (数据模板)
│   ├── v1                    (APP)
│   │   ├── __init__.py
│   │   ├── controllers.py
│   │   └── router.py         (绑定路由)
│   ├── __init__.py
│   ├── config.py             (加载配置文件)
│   ├── server.py             (服务入口文件)
│   └── wsgi.py               (Routes相关)
└── requirements.txt          (项目包依赖)

```

# 3、API接口文档

## 依赖安装

1、安装[nodejs](https://nodejs.org/)

> sudo apt-get install nodejs

2、更改为[淘宝源](http://npm.taobao.org/)

> sudo npm install -g cnpm --registry=https://registry.npm.taobao.org

3、安装[apidoc](http://apidocjs.com/)

> sudo cnpm install apidoc -g

## apidoc语法

详见[官网](http://apidocjs.com/)(需翻墙)

## 更新接口文档

cd 到项目根目录

> apidoc -i ./ -o apidoc/


# 4、压力测试

1. 指令:
`ab -n 1000 -c 10 http://127.0.0.1:8088/v1/users/1`

结果:

```
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:
Server Hostname:        127.0.0.1
Server Port:            8088

Document Path:          /v1/users/1
Document Length:        23 bytes

Concurrency Level:      10
Time taken for tests:   2.917 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      150000 bytes
HTML transferred:       23000 bytes
Requests per second:    342.84 [#/sec] (mean)
Time per request:       29.168 [ms] (mean)
Time per request:       2.917 [ms] (mean, across all concurrent requests)
Transfer rate:          50.22 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       3
Processing:     4   29   5.3     27      58
Waiting:        3   28   5.3     27      58
Total:          4   29   5.3     27      59

Percentage of the requests served within a certain time (ms)
  50%     27
  66%     29
  75%     30
  80%     31
  90%     33
  95%     36
  98%     52
  99%     55
 100%     59 (longest request)

```

2. 指令: `ab -n 1000 -c 100 http://127.0.0.1:8088/v1/users/1`

结果:

```
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
apr_socket_recv: Connection reset by peer (54)
Total of 430 requests completed

```