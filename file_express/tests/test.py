# -*- coding: utf-8 -*-

from com_tf.lib.com import Com


def test():
    com = Com()
    print(com.read_lock is com.lock)


if __name__ == '__main__':
    test()
