# -*- coding: utf-8 -*-


class Singleton(type):
    def __init__(cls, name, bases, _dict):
        super(Singleton, cls).__init__(name, bases, _dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance
