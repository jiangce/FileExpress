# -*- coding: utf-8 -*-

from ..manager.sch import JobScheduler as JS
from ..observer.observer import Observer


@JS.register('监听')
def observe():
    obs = Observer()
    obs.start()
