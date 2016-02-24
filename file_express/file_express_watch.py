# -*- coding: utf-8 -*-

import psutil
import os
from file_express.lib.singleton import Singleton
from file_express.manager.env import Environment


class FileExpressWatch(metaclass=Singleton):
    def __init__(self):
        self.env = Environment()

    def find_process(self):
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if p.name() == 'fexp.exe':
                return p

    def kill(self, p=None):
        p = p or self.find_process()
        if p:
            p.kill()

    def run(self):
        if not self.find_process():
            bat = os.path.join(self.env.work_path, 'fexp.bat')
            with open(bat, 'w') as f:
                f.write('fexp.exe')
            os.startfile(bat)


def watch():
    """
    配置进程监视作业，1或2分钟一次
    """
    FileExpressWatch().run()
