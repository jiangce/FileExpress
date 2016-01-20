# -*- coding: utf-8 -*-

from .emitter_base import EmitterBase
from ..lib.ftp_util import FTP
from socket import _GLOBAL_DEFAULT_TIMEOUT


class FtpEmitter(EmitterBase):
    def __init__(self, emit_dir, scanner_names=None, filters=None,
                 ftp_ip='localhost', ftp_port=0,
                 ftp_name='', ftp_pass='', ftp_encoding='utf-8',
                 ftp_timeout=_GLOBAL_DEFAULT_TIMEOUT):
        super(FtpEmitter, self).__init__(scanner_names, filters)
        self.__emit_dir__ = emit_dir
        self.ftp = FTP(ftp_ip, ftp_port, ftp_name, ftp_pass, ftp_encoding, ftp_timeout)

    def connect_ftp(self):
        if not self.ftp.connected:
            self.ftp.connect()
        try:
            self.ftp.cd(self.__emit_dir__)
            return True
        except:
            return False

    def rename_file(self, old_file_name, new_file_name):
        if self.connect_ftp():
            self.ftp.rename(old_file_name, new_file_name)

    def emit_file(self, source_fullname, target_name):
        try:
            if self.connect_ftp():
                self.ftp.upload(source_fullname, target_name)
                return True
            return False
        except:
            return False

    def scan_files(self):
        return self.ftp.getfiles() if self.connect_ftp() else []

    def exists(self, file_name):
        return file_name in self.scan_files()

    def delete_file(self, file_name):
        try:
            if self.connect_ftp():
                self.ftp.delfile(file_name)
                return True
            return False
        except:
            return False
