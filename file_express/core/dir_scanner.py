# -*- coding: utf-8 -*-

from .scanner_base import ScannerBase
import os


class DirScanner(ScannerBase):
    def __init__(self, name, scan_dir, filters=None):
        super(DirScanner, self).__init__(name, filters)
        self.scan_dir = scan_dir

    def scan_files(self):
        return [name for name in os.listdir(self.scan_dir) if os.path.isfile(os.path.join(self.scan_dir, name))]

    def exists(self, file_name):
        return os.path.exists(os.path.join(self.scan_dir, file_name))

    def obtain_file(self, file_name, target_fullname):
        try:
            os.rename(os.path.join(self.scan_dir, file_name), target_fullname)
            return True
        except:
            return False

    def delete_file(self, file_name):
        try:
            os.remove(os.path.join(self.scan_dir, file_name))
            return True
        except:
            return False
