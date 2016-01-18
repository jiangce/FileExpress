# -*- coding: utf-8 -*-

from file_express.core.dir_scanner import DirScanner
from file_express.core.dir_emitter import DirEmitter
from file_express.core.manager import ExpressManager

scanner = DirScanner('test', r'C:\togeek\test\1', '*')
emitter = DirEmitter(r'C:\togeek\test\2', '*', '*')

manager = ExpressManager()
manager.add_scanners(scanner)
manager.add_emitters(emitter)

manager.scan()
manager.emit()
