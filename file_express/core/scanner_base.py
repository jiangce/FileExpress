# -*- coding: utf-8 -*-

import abc
import fnmatch
from .manager import ExpressManager
from ..lib.filter_util import get_filter_set


class ScannerBase(metaclass=abc.ABCMeta):
    def __init__(self, name, filters=None):
        self.name = name
        self.manager = ExpressManager()
        self.__filters__ = get_filter_set(filters)

    def filter(self, file_name):
        return any([fnmatch.fnmatch(file_name, f) for f in self.__filters__])

    @abc.abstractmethod
    def scan_files(self):
        return []

    @abc.abstractmethod
    def exists(self, file_name):
        return True

    @abc.abstractmethod
    def delete_file(self, file_name):
        return True

    @abc.abstractmethod
    def obtain_file(self, file_name, target_fullname):
        return True
