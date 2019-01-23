"""
@Time    : 2019/1/23 17:15
@Author  : Sam
@Project : pyinfluxdb
@FileName: test_find_timespan.py
@Software: PyCharm
@Blog    : https://blog.muumlover.com
"""
from pyinfluxdb import FILL


def test_find_timespan():
    import pytz
    import random
    from datetime import datetime, timedelta
    from pyinfluxdb import InfluxClient
    tz = pytz.timezone('Asia/Shanghai')
    number = random.randint(0, 99)
    value = random.randint(0, 99)
    speed = random.randint(0, 99)
    client = InfluxClient(timezone=tz.zone)
    db = client.get_database('test_db')
    measure = db.get_measurement('test_measure')
    measure.insert_one(tags={'number': number}, fields={'value': value, 'speed': speed})
    point = measure.last(
        filter={'time': {'>': datetime.now(tz=tz) - timedelta(days=1)}},
        fields='speed',
        time_span='1h',
        fill_type=FILL.PREVIOUS)
    assert point.get('value', None) == value
    assert point.get('speed', None) == speed
    assert datetime.now(tz=tz) - point.get('time', None) < timedelta(minutes=1)


if __name__ == '__main__':
    test_find_timespan()
