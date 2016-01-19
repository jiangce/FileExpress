# -*- coding: utf-8 -*-

from ..manager.sch import JobScheduler
from ..core.config import Config


def init_jobs():
    from . import job
    js = JobScheduler()
    config = Config()
    manager = config.get_express_manager()
    js.add_interval_job('scan', seconds=1, func_args=[manager])
    js.add_interval_job('emit', seconds=1, func_args=[manager])
