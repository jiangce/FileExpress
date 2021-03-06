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

    def connect_ftp(self):
        if not self.ftp.connected:
            self.ftp.connect()
        try:
            self.ftp.cd(self.scan_dir)
            return True
        except:
            return False

    def scan_files(self):
        return self.ftp.getfiles() if self.connect_ftp() else []

    def exists(self, file_name):
        return file_name in self.scan_files()

    def obtain_file(self, file_name, target_fullname):
        localpath, localname = os.path.split(target_fullname)
        try:
            if self.connect_ftp():
                self.ftp.download(file_name, localpath, localname)
                return True
            return False
        except:
            return False

    def delete_file(self, file_name):
        try:
            if self.connect_ftp():
                self.ftp.delfile(file_name)
                return True
            return False
        except:
            return False
