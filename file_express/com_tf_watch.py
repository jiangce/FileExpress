# -*- coding: utf-8 -*-

import psutil
import os
import time
from .lib.singleton import Singleton
from .lib.env import Environment


class ComTFWatch(metaclass=Singleton):
    def __init__(self):
        self.env = Environment()
        self.tick = os.path.join(self.env.send_path, '.tick')

    def tick_exist(self):
        return os.path.exists(self.tick)

    def generate_tick(self):
        try:
            if not self.tick_exist():
                tmp = self.tick + '.tmp'
                with open(tmp, 'w') as f:
                    f.write('.')
                os.rename(tmp, self.tick)
        except:
            pass

    def del_tick(self):
        try:
            if os.path.exists(self.tick):
                os.remove(self.tick)
        except:
            pass

    def restart(self):
        if self.tick_exist():
            self.del_tick()
            self.kill()
            time.sleep(1)
            self.run()
            return True
        else:
            return False

    def find_process(self):
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if p.name() == 'comtf.exe':
                return p

    def kill(self, p=None):
        p = p or self.find_process()
        if p:
            p.kill()

    def run(self):
        p = self.find_process()
        if p:
            if not self.restart():
                self.generate_tick()
                time.sleep(30)
                self.restart()
        else:
            bat = os.path.join(self.env.root, 'com_tf.bat')
            with open(bat, 'w') as f:
                f.write('comtf.exe')
            os.startfile(bat)


def watch():
    """
    配置进程监视作业，1或2分钟一次
    """
    com = ComTFWatch()
    com.run()
