# -*- coding: utf-8 -*-

from ..manager.sch import JobScheduler as JS
from ..manager.env import Environment
import os
import datetime


@JS.register('scan')
def scan(manager):
    manager.scan()


@JS.register('emit')
def emit(manager):
    manager.emit()


@JS.register('del_backup')
def del_backup():
    env = Environment()
    backup_path = os.path.join(env.work_path, 'backup')
    for file_name in os.listdir(backup_path):
        full_name = os.path.join(backup_path, file_name)
        file_time = datetime.datetime.fromtimestamp(os.path.getmtime(full_name))
        delta = datetime.datetime.now() - file_time
        if delta.days > 7:
            os.remove(full_name)
