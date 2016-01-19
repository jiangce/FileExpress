# -*- coding: utf-8 -*-

from ..manager.sch import JobScheduler as JS


@JS.register('scan')
def scan(manager):
    manager.scan()


@JS.register('emit')
def emit(manager):
    manager.emit()
