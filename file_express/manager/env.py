# -*- coding: utf-8 -*-

import winreg
from ..lib.singleton import Singleton


class Environment(metaclass=Singleton):
    def __init__(self, root=winreg.HKEY_LOCAL_MACHINE):
        assert root in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
        self.__root__ = root
        self.work_path = None
        self.error_count = 0
        try:
            self.load_config()
        except FileNotFoundError:
            print('尚未初始化环境变量')

    def write_config(self, work_path, error_count=5):
        with winreg.CreateKeyEx(self.__root__, r'SOFTWARE\ToGeek\file_express') as key:
            winreg.SetValueEx(key, 'work_path', 0, winreg.REG_SZ, work_path)
            winreg.SetValueEx(key, 'error_count', 0, winreg.REG_DWORD, error_count)
        self.load_config()

    def load_config(self):
        with winreg.OpenKeyEx(self.__root__, r'SOFTWARE\ToGeek\file_express') as key:
            self.work_path = winreg.QueryValueEx(key, 'work_path')[0]
            self.error_count = winreg.QueryValueEx(key, 'error_count')[0]

    def __str__(self):
        return 'work_path: %s\n' % self.work_path + \
               'error_count: %s' % self.error_count
