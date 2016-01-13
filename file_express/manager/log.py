# -*- coding: utf-8 -*-

import os
import sys
import logging
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler
from ..lib.singleton import Singleton
from .env import Environment


class Log(metaclass=Singleton):
    def __init__(self, level=logging.INFO, print_std=True):
        self.name = 'file_express'
        self.env = Environment()
        self._logger = logging.getLogger(self.name)
        self._logger.setLevel(level)
        self._logger.handlers.clear()
        log_format_str = '%(asctime)s\n' \
                         '[%(levelname)s][%(module)s][PID: %(process)d][TID: %(thread)d] - %(message)s\n'
        log_format = logging.Formatter(log_format_str)
        self.path = os.path.join(self.env.work_path, 'log')
        if self.path:
            self.file = os.path.join(self.path, 'log.txt')
            if not os.path.exists(self.path):
                os.mkdir(self.path)
            log_handler = TimedRotatingFileHandler(self.file, when='h', interval=1, backupCount=24)
            log_handler.setFormatter(log_format)
            self._logger.addHandler(log_handler)

        if print_std:
            log_handler = StreamHandler(sys.stdout)
            log_handler.setFormatter(log_format)
            self._logger.addHandler(log_handler)

    @property
    def logger(self):
        return self._logger
