# -*- coding: utf-8 -*-

import os
import json
from ..manager.env import Environment
from ..lib.singleton import Singleton
from .manager import ExpressManager
from .dir_scanner import DirScanner
from .dir_emitter import DirEmitter

__mapping__ = {'dir_scanner': DirScanner,
               'dir_emitter': DirEmitter}


class Config(metaclass=Singleton):
    def __init__(self):
        self.env = Environment()
        self.config_file = os.path.join(self.env.work_path, 'config.json')

    def read_config(self):
        def args(params):
            del params['type']
            return params

        with open(self.config_file, encoding='utf-8') as f:
            config = json.load(f)
        return [__mapping__[p['type']](**args(p)) for p in config['scanners'] if p['type'] in __mapping__], \
               [__mapping__[p['type']](**args(p)) for p in config['emitters'] if p['type'] in __mapping__]

    def get_express_manager(self):
        scanners, emitters = self.read_config()
        manager = ExpressManager()
        manager.add_scanners(*scanners)
        manager.add_emitters(*emitters)
        return manager
