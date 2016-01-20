# -*- coding: utf-8 -*-

import abc
import fnmatch
from .manager import ExpressManager
from ..lib.filter_util import get_filter_set


class EmitterBase(metaclass=abc.ABCMeta):
    def __init__(self, scanner_names, filters):
        self.__scanner_names__ = get_filter_set(scanner_names)
        self.__filters__ = get_filter_set(filters)
        self.manager = ExpressManager()

    def filter(self, scanner_name, file_name):
        return any([fnmatch.fnmatch(scanner_name, f) for f in self.__scanner_names__]) and \
               any([fnmatch.fnmatch(file_name, f) for f in self.__filters__])

    @abc.abstractmethod
    def exists(self, file_name):
        return True

    @abc.abstractmethod
    def delete_file(self, file_name):
        return True

    @abc.abstractmethod
    def rename_file(self, old_file_name, new_file_name):
        pass

    @abc.abstractmethod
    def emit_file(self, source_fullname, target_name):
        return True
