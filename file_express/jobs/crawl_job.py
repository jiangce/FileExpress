# -*- coding: utf-8 -*-

from ..manager.sch import JobScheduler as JS
from ..crawler.sn_hdpt import SNHdpt
from ..lib.file_util import write_obj


@JS.register('陕西取数')
def sn_crawl():
    sn_hdpt_crawler = SNHdpt()
    result = sn_hdpt_crawler.start()
    write_obj('sn_3z_data', result)
