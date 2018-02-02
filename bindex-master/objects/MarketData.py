import math
from Models import Price, Funds
from Database import db_session
from Utilities import Utilities
from dateutil import parser
from datetime import datetime, timedelta, time

from operator import itemgetter
import operator
import itertools

import json
from flask import jsonify


from sqlalchemy.sql import select
from sqlalchemy import or_, desc, asc

util = Utilities()
dateTime = util.dateTime()
price = Price()
funds = Funds()


class MarketData:
    def __init__(self):
        pass

    def getCalculation(self, amount):
        amount = int(amount)
        end = 140967
        start = 5000
        growth = (end-start) / amount
        print growth

        result = ( amount * growth ) + amount

        return result

    def dateToEpoch(self, date):
        calc = parser.parse(date) - datetime(1970,1,1)
        return calc.total_seconds()

    def epochToDate(self, epoch):
        date = datetime.fromtimestamp(epoch).strftime('%c')
        return date

    def historicalData(self, time, items):

        input_time = int(time)
        today_time = parser.parse(dateTime['today'])

        prior_time = today_time - timedelta(seconds=input_time)

        responses = []
        for item in items:
            response = price.query.filter(Price.symbol == item).order_by(asc(Price.date)).all()
            cumsum = 0
            for r in response:
                item_date = parser.parse(str(r.date))
                #perform checks on each data field
                if prior_time <= item_date <= today_time:
                    cumsum += float(r.change)
                    f = {}
                    f['name'] = r.name
                    f['symbol'] = r.symbol
                    f['date'] = item_date
                    f['date_sec'] = item_date.strftime('%s')
                    f['price'] = float(r.price)
                    f['change'] = float(r.change)
                    f['cum_change'] = cumsum
                    responses.append(f)

        return sorted(responses, key=itemgetter('name','date'))


    def recentThreeItems(self):
        item = []
        for u in price.query.filter(or_(Price.symbol == 'SP', Price.symbol == 'BTC', Price.symbol == 'BINDEX')).order_by(Price.date.desc()).limit(2):
            item.append(u.__dict__)

        return item

    def removeDupeDays(self, dct):
        # getVals = itemgetter('date', 'symbol', 'price')
        # dct.sort(key=getVals)
        # print dct
        #
        # result = []
        # for k, v in itertools.groupby(dct, getVals):
        #     result.append(v.next())
        # dct[:] = result
        #
        # print dct
        return ''

    def getAllHistoricalData(self):
        return price.query.all()
        # return json.dumps(Price.serialize_list(price)

    def getHistoricalBindexData(self, time, amount, type):
        portfolio = funds.query.all() #these are the percents/symbols json
        items = []
        dictionary = []

        for p in portfolio:
            f = {}
            f['symbol'] = p.symbol
            f['percent'] = p.percent
            items.append(f) #convert SQL query into an array of dictionaries with symbol and percent

        for coin in items:
            days = price.query.filter(Price.symbol == items['symbols']).order_by(asc(Price.date)).all()
            bindex_sum = 0
            for coin_day in days:
                bindex_sum += (float(coin_day['price']) * float(coin.percent))
                f = {}
                f['bindex_value'] = bindex_sum
                f['date'] = coin_day['date']
                f['symbol'] = coin_day['symbol']
                dictionary.append(f)
            print days

        return items

        # return ''

    def predictiveData(self, amount, time, type):
        #create trend line using existing historical data
        #And apply that trend line to one point 6+ months from now

        #amount = amount of dollars initially invested assuming today
        #time = time of investing (e.g. 6 months, 1 year, etc.)
        #type = fund type

        return ''
