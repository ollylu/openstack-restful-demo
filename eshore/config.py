# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `config`
    @Author : `long`
    @Date   : `2016-05-26`
    @About  : ''
"""
import ConfigParser
import os

config_file_name = 'development.conf'
config_parser = ConfigParser.ConfigParser()
# 获取上层目录的路径
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
file_path = project_path + '/etc/' + config_file_name
# 读取配置文件
config_parser.read(file_path)


DB_CONFIG = dict(config_parser.items("database"))
PASTE_CONFIG = project_path + '/etc/paste_config.ini'
APP_NAME = 'openstack'

