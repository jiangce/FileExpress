# -*- coding: utf-8 -*-

from .scanner_base import ScannerBase
from ..lib.ftp_util import FTP
from socket import _GLOBAL_DEFAULT_TIMEOUT
import os


class FtpScanner(ScannerBase):
    def __init__(self, name, scan_dir, filters=None,
                 ftp_ip='localhost', ftp_port=0,
                 ftp_name='', ftp_pass='', ftp_encoding='utf-8',
                 ftp_timeout=_GLOBAL_DEFAULT_TIMEOUT):
        super(FtpScanner, self).__init__(name, filters)
        self.scan_dir = scan_dir
        self.ftp = FTP(ftp_ip, ftp_port, ftp_name, ftp_pass, ftp_encoding, ftp_timeout)

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
