"""
@Time    : 2019/1/16 10:16
@Author  : Sam
@Project : pyinfluxdb
@FileName: test_insert_one.py
@Software: PyCharm
@Blog    : https://blog.muumlover.com
"""
from dateutil import parser


def test_insert_one():
    import pytz
    import random
    from datetime import datetime, timedelta
    from pyinfluxdb import InfluxClient
    tz = pytz.timezone('Asia/Shanghai')
    number = random.randint(0, 99)
    value = random.randint(0, 99)
    speed = random.randint(0, 99)
    client = InfluxClient(timezone=tz.zone)
    db = client.test_db
    measure = db.test_measure
    measure.insert_one(tags={'number': number}, fields={'value': value, 'speed': speed})
    point = measure.find_one({'number': number})
    assert point is not None
    assert point.get('value', None) == value
    assert point.get('speed', None) == speed
    assert datetime.now(tz=tz) - parser.parse(point.get('time', None)) < timedelta(minutes=1)


def test_insert_one_2():
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
    point = measure.find_one({'number': number})
    assert point.get('value', None) == value
    assert point.get('speed', None) == speed
    assert datetime.now(tz=tz) - point.get('time', None) < timedelta(minutes=1)


if __name__ == '__main__':
    test_insert_one()
