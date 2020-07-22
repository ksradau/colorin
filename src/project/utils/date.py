from datetime import date
from datetime import datetime

from delorean import Delorean


def utcnow() -> datetime:
    return Delorean().datetime


def near(dt1: datetime, dt2: datetime, interval=0):
    delta = abs(dt1 - dt2)
    return delta.total_seconds() <= interval
