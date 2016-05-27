# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `models`
    @Author : `long`
    @Date   : `2016-05-26`
    @About  : ''
"""

from sqlalchemy import (Column, Index, Integer, BigInteger, Enum, String,
                        schema, Unicode)

from eshore.db import session, Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    password = Column(String(25))

    def __repr__(self):
        return "<User(name='%s')>" % self.name

    @staticmethod
    def create_user(data):
        pass
