import datetime

import redis
import requests

r = redis.Redis(host="homestead.test", port=6379, decode_responses=True)

def getDate():
    year = datetime.date.today().year
    max_date = datetime.date(year, 12, 31)
    min_date = datetime.date(year, 1, 1)

    date_list = []

    _date = min_date
    while (_date <= max_date):
        date_list.append(_date)
        _date = _date + datetime.timedelta(days=1)

    date_list = list(
        map(lambda date_time: date_time.strftime("%Y%m%d"), date_list))

    return date_list


def getStatus(date_list):
    for _date in date_list:
        response = requests.get(
            f"http://api.goseek.cn/Tools/holiday?date={_date}")
        r.set(_date, response.json()['data'])


def order(date_list):
    _workday = []
    _holiday = []
    for _date in date_list:
        date_type = r.get(_date)
        if int(date_type) in (1, 3):
            _holiday.append(_date)
        else:
            _workday.append(_date)
    _workday.sort()
    _holiday.sort()

    for index, key in enumerate(_holiday):
        r.zadd('holiday',{f"{key}":index+1})

    for index, key in enumerate(_workday):
        r.zadd('workday',{f"{key}":index+1})

date_list = getDate()
getStatus(date_list)
order(date_list)
