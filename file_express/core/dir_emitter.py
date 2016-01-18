# -*- coding: utf-8 -*-

from .emitter_base import EmitterBase
import os
import shutil


class DirEmitter(EmitterBase):
    def __init__(self, emit_dir, scanner_names, filters):
        super(DirEmitter, self).__init__(scanner_names, filters)
        self.__emit_dir__ = emit_dir

    def rename_file(self, old_file_name, new_file_name):
        return os.rename(os.path.join(self.__emit_dir__, old_file_name),
                         os.path.join(self.__emit_dir__, new_file_name))

    def emit_file(self, source_fullname, target_name):
        try:
            shutil.copy(source_fullname, os.path.join(self.__emit_dir__, target_name))
            return True
        except:
            return False

    def exists(self, file_name):
        return os.path.exists(os.path.join(self.__emit_dir__, file_name))

    def delete_file(self, file_name):
        try:
            os.remove(os.path.join(self.__emit_dir__, file_name))
            return True
        except:
            return False
