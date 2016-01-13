# -*- coding: utf-8 -*-

from ..manager.sch import JobScheduler


def init_jobs():
    from . import crawl_job, observe_job
    js = JobScheduler()
    js.add_interval_job('陕西取数', hours=1)
    js.add_started_job('监听')
