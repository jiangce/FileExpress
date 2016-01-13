# -*- coding: utf-8 -*-

import datetime
import re


class DateTimeParser:
    def __init__(self, date=None, time=None):
        self.p_date = re.compile(r'(\d+)-(\d+)-(\d+)')
        self.p_time = re.compile(r'(\d+):(\d+):?(\d+)?.*')
        self.datetime = datetime.datetime(1, 1, 1, 0, 0, 0)
        self.set_date(date)
        self.set_time(time)

    def verify_date(self, date):
        date = list(date)[0:3]
        if date[0] < 100:
            date[0] += 2000
        if date[1] < 1 or date[1] > 12:
            raise Exception('error month')
        if date[2] < 1 or date[2] > 31:
            raise Exception('error day')
        return self.datetime.replace(*date)

    def verify_time(self, time):
        time = list(time)[0:3]
        if len(time) == 2:
            time.append(0)
        h = time[0] % 24
        dh, time[0] = time[0] - h, h
        m = time[1] % 60
        dm, time[1] = time[1] - m, m
        s = time[2] % 60
        ds, time[2] = time[2] - s, s
        return self.datetime.replace(hour=time[0], minute=time[1], second=time[2]) \
               + datetime.timedelta(hours=dh, minutes=dm, seconds=ds)

    def set_date(self, date):
        if isinstance(date, str):
            m = self.p_date.search(date)
            if m:
                self.datetime = self.verify_date(map(int, m.groups()))
        elif isinstance(date, (list, tuple)):
            self.datetime = self.verify_date(date)
        elif isinstance(date, (datetime.date, datetime.datetime)):
            self.datetime = self.verify_date(date.timetuple())
        return self

    def set_time(self, time):
        if isinstance(time, str):
            m = self.p_time.search(time)
            if m:
                self.datetime = self.verify_time(map(lambda x: int(x) if x is not None else 0, m.groups()))
        elif isinstance(time, (list, tuple)):
            self.datetime = self.verify_time(time)
        elif isinstance(time, datetime.datetime):
            self.datetime = self.verify_time(time.timetuple()[3:6])
        elif isinstance(time, datetime.time):
            self.datetime = self.verify_time((time.hour, time.minute, time.second))
        return self
