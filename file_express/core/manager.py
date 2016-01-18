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

    def add_emitters(self, *emitters):
        self.__emitters__.extend(emitters)

    def add_scanners(self, *scanners):
        self.__scanners__.extend(scanners)

    def scanner_path(self, scanner):
        path = os.path.join(self.exchange, scanner.name)
        backup_path = os.path.join(self.backup, scanner.name)
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(backup_path):
            os.mkdir(backup_path)
        return path, backup_path

    def scanner_obtain_files(self, scanner):
        for file_name in scanner.scan_files():
            if file_name.lower().endswith('.tmp'):
                continue
            target_file = os.path.join(self.scanner_path(scanner)[0], file_name)
            tmp_file = target_file + '.tmp'
            if scanner.filter(file_name) and scanner.exists(file_name):
                if os.path.exists(tmp_file):
                    os.remove(tmp_file)
                if os.path.exists(target_file):
                    os.remove(target_file)
                if scanner.obtain_file(file_name, tmp_file):
                    os.rename(tmp_file, target_file)
                scanner.delete_file(file_name)

    def scan(self):
        for scanner in self.__scanners__:
            self.scanner_obtain_files(scanner)

    def emit_file(self, scanner_name, file_name):
        if file_name.lower().endswith('.tmp'):
            return
        for emitter in self.__emitters__:
            if emitter.filter(scanner_name, file_name):
                source_file = os.path.join(self.exchange, scanner_name, file_name)
                tmp_file = file_name + '.tmp'
                if emitter.exists(file_name):
                    emitter.delete_file(file_name)
                if emitter.exists(tmp_file):
                    emitter.delete_file(tmp_file)
                if os.path.exists(source_file) and emitter.emit_file(source_file, tmp_file):
                    emitter.rename_file(tmp_file, file_name)
        self.backup_file(scanner_name, file_name)

    def backup_file(self, scanner_name, file_name):
        source = os.path.join(self.exchange, scanner_name, file_name)
        target = os.path.join(self.backup, scanner_name, file_name)
        if os.path.exists(target):
            os.remove(target)
        os.rename(source, target)

    def emit(self):
        for scanner in self.__scanners__:
            path = self.scanner_path(scanner)[0]
            for file_name in os.listdir(path):
                if os.path.isfile(os.path.join(path, file_name)):
                    self.emit_file(scanner.name, file_name)
