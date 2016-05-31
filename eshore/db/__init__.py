# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `__init__.py`
    @Author : `long`
    @Date   : `2016-05-26`
    @About  : ''
"""

from sqlalchemy import create_engine
from eshore import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

db_url = "mysql://%s:%s@%s:%s/%s" % (
    config.DB_CONFIG['user'],
    config.DB_CONFIG['password'],
    config.DB_CONFIG['host'],
    config.DB_CONFIG['port'],
    config.DB_CONFIG['name']
)
db = create_engine(db_url, echo=True)
Base = declarative_base()
session = scoped_session(sessionmaker(bind=db))
Base.query = session.query_property()


def init_db():
    from eshore.db.models import User
    Base.metadata.create_all(bind=db)

