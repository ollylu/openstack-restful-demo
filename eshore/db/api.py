# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `api`
    @Author : `long`
    @Date   : `2016-05-26`
    @About  : ''
"""
from eshore.db import session
from eshore.db.models import User


def show_users(user_id):
    """
    show user information
    :param user_id:
    :return:
    """
    try:
        return session.query(User).filter(User.id == user_id).one()
    except:
        return False


def create_user(data):
    """
    create user
    :param data:
    :return:
    """
    if session.query(User).filter(User.id == data['id']).one_or_none():
        return False
    else:
        user = User(**data)
        session.add(user)
        session.flush()
        session.commit()
        return True


