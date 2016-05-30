# 项目框架

![](http://o6p181fdf.bkt.clouddn.com/16-5-27/18951712.jpg)


# 项目目录结构


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

# API接口文档

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
