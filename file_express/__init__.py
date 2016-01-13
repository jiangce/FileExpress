# -*- coding: utf-8 -*-

import sys
from .lib.parse_input import get_input
from .manager.env import Environment
from .manager.sch import JobScheduler
from .manager.log import Log
from .jobs import init_jobs

version = '1.0.0'
env = Environment()


def init_env():
    work_path = get_input('工作路径：', default=r'c:\togeek')
    error_count = get_input('错误重试次数：', int, 5)
    env.write_config(work_path, error_count)
    print(env)


def main():
    if '--config' in sys.argv:
        init_env()
        return
    Log(print_std='--print' in sys.argv).logger.info('ToGeek File Express Started...')
    init_jobs()
    JobScheduler().scheduler.start()
