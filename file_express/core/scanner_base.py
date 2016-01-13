# -*- coding: utf-8 -*-

import abc
from .manager import ExpressManager


class ScannerBase(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name
        self.manager = ExpressManager()

    @abc.abstractmethod
    def scan_files(self):
        return []

    @abc.abstractmethod
    def filter(self, file_name):
        return True

    @abc.abstractmethod
    def exists(self, file_name):
        return True

    @abc.abstractmethod
    def delete_file(self, file_name):
        return True

    @abc.abstractmethod
    def obtain_file(self, file_name, target_fullname):
        return True
