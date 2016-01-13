# -*- coding: utf-8 -*-

from .scanner_base import ScannerBase
import fnmatch


class DirScanner(ScannerBase):
    def __init__(self, name, _filter=None):
        super(DirScanner, self).__init__(name)
        if isinstance(_filter, str):
            _filter = {_filter}
        elif isinstance(_filter, (tuple, list, set)):
            _filter = set(_filter)
        else:
            _filter = {'*'}
        self.__filter_set__ = _filter

    def filter(self, file_name):
        return any([fnmatch.fnmatch(file_name, f) for f in self.__filter_set__])

    def scan_files(self):
        pass

    def exists(self, file_name):
        pass

    def obtain_file(self, file_name, target_fullname):
        pass

    def delete_file(self, file_name):
        pass
