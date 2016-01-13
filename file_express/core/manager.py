# -*- coding: utf-8 -*-

from ..manager.env import Environment
from ..lib.singleton import Singleton
import os


class ExpressManager(metaclass=Singleton):
    def __init__(self):
        self.env = Environment()
        self.exchange = os.path.join(self.env.work_path, 'exchange')
        if not os.path.exists(self.exchange):
            os.mkdir(self.exchange)
        self.backup = os.path.join(self.env.work_path, 'backup')
        if not os.path.exists(self.backup):
            os.mkdir(self.backup)
        self.__scanners__ = []
        self.__emitters__ = []

    def scanner_path(self, scanner):
        path = os.path.join(self.exchange, scanner.name)
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def scanner_obtain_files(self, scanner):
        for file_name in scanner.scan_files():
            if file_name.lower().endswith('.tmp'):
                continue
            target_file = os.path.join(self.scanner_path(scanner), file_name)
            tmp_file = target_file + '.tmp'
            if scanner.filter(file_name) and scanner.exists(file_name):
                if os.path.exists(tmp_file):
                    os.remove(tmp_file)
                if os.path.exists(target_file):
                    os.remove(target_file)
                if scanner.obtain_file(file_name, tmp_file):
                    os.rename(tmp_file, target_file)
                scanner.delete_file(file_name)
