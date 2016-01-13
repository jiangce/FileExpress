# -*- coding: utf-8 -*-

import os
from .lib.env import Environment
from .lib.log import Log
from .protocol_session import *


def onsuccess(session):
    Log().logger.info('[%s] %s -> send success' % (session.sid, session.filename))
    if session.issender:
        os.remove(session.fullname)


def onexists(session):
    Log().logger.info('[%s] %s -> file exists, delete it' % (session.sid, session.filename))
    if not session.issender:
        os.remove(session.fullname)


def initialize():
    pool = SessionPool()
    pool.onexists = onexists
    pool.onsuccess = onsuccess
    init()


def transfer_files():
    env = Environment()
    for name in os.listdir(env.send_path):
        if len(getoutfiles()) >= 3:
            break
        fullname = os.path.join(env.send_path, name)
        if not os.path.isfile(fullname) or name.lower().endswith('.tmp'):
            continue
        transfer(fullname)


def closeAll():
    close()
