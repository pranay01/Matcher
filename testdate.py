import time

class Date(object):
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @staticmethod
    def now():
        t=time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    @staticmethod
    def tomorrow():
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


