# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from ..lib.singleton import Singleton
from ..lib.date_time_parser import DateTimeParser
from ..manager.log import Log


class JobScheduler(metaclass=Singleton):
    __function_dict__ = {}

    def __init__(self):
        self.logger = Log().logger
        self.scheduler = BlockingScheduler(logger=self.logger)
        self.parser = DateTimeParser()

    def get_lives(self):
        return {job.name: job for job in self.scheduler.get_jobs()}

    def add_job(self, name, trigger, trigger_args, func_args=None, func_kwargs=None):
        if name not in self.get_lives():
            func = self.get_functions(name)
            self.scheduler.add_job(func, trigger=trigger, args=func_args, kwargs=func_kwargs,
                                   id=name, name=name, **trigger_args)
            self.logger.info('[%s][%s]作业已添加，并已启动' % (trigger, name))

    def add_date_job(self, name, time, func_args=None, func_kwargs=None):
        time = self.parser.set_date(time).set_time(time).datetime
        self.add_job(name, 'date', {'run_date': time}, func_args, func_kwargs)

    def add_interval_job(self, name, weeks=0, days=0, hours=0, minutes=0, seconds=0,
                         func_args=None, func_kwargs=None):
        self.add_job(name, 'interval',
                     {'weeks': weeks, 'days': days,
                      'hours': hours, 'minutes': minutes, 'seconds': seconds},
                     func_args, func_kwargs)

    def add_cron_job(self, name, year=None, month=None, day=None, week=None,
                     day_of_week=None, hour=None, minute=None, second=None,
                     func_args=None, func_kwargs=None):
        self.add_job(name, 'cron',
                     {'year': year, 'month': month, 'day': day, 'week': week,
                      'day_of_week': day_of_week,
                      'hour': hour, 'minute': minute, 'second': second},
                     func_args, func_kwargs)

    def add_started_job(self, name, after_seconds=1, func_args=None, func_kwargs=None):
        time = datetime.now() + timedelta(seconds=after_seconds)
        self.add_date_job(name, time, func_args, func_kwargs)

    def delete_job(self, name):
        jobs = self.get_lives()
        if name in jobs:
            self.scheduler.remove_job(jobs[name].id)
            self.logger.info('作业[%s]已移除' % name)

    @classmethod
    def register(cls, name):
        def add_method(f):
            cls.__function_dict__[name.strip()] = f
            return f

        return add_method

    def get_functions(self, name):
        return self.__function_dict__.get(name.strip())

    def get_function_doc(self, name):
        return self.get_functions(name).__doc__

    def get_function_names(self):
        return sorted(self.__function_dict__.keys())
