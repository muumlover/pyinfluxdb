"""
@Time    : 2019/1/16 10:16
@Author  : Sam
@Project : pyinfluxdb
@FileName: test_insert.py
@Software: PyCharm
@Blog    : https://blog.muumlover.com
"""

from pyinfluxdb import InfluxClient

if __name__ == '__main__':
    client = InfluxClient()
    db = client.test_db
    measure = db.test_measure
    measure.insert_one(tags={'number': '01'}, fields={'value': 0, 'speed': 2})
    a = measure.find({'number': '01', 'time': {'>': '2019-01-16 15:50:00'}})
    # a = measure.find_one()
    print(a)
    # parsed_date = parser.parse(a.get('time',''))
    # print(parsed_date)
    # print(parsed_date.strftime('%Y-%m-%d %H:%M:%S'))
    pass
