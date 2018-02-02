import json
import requests
from urllib import urlopen
from bs4 import BeautifulSoup

from Models import Price
from Database import db_session
from Utilities import Utilities
import re

util = Utilities()
dateTime = util.dateTime()

class WebScrapers:
    def __init__(self):
        pass

    def getCoinPrice(self):
        url = urlopen('https://api.coinmarketcap.com/v1/ticker/').read()
        response = json.loads(url)

        coins = []
        for item in response:
            f = {}
            f['symbol'] = str(item['symbol'])
            f['name'] = str(item['name'])
            f['market_cap'] = str(item['market_cap_usd'])
            f['price'] = str(item['price_usd'])
            f['change'] = str(item['percent_change_24h'])
            f['date'] = str(dateTime['today'])
            coins.append(f)

        return coins

    def getMarketQuote(self, symbol):
      url = 'https://finance.google.com/finance?q=' + symbol
      r = requests.get(url)
      data = r.text.encode('utf-8').decode('ascii', 'ignore')
      soup = BeautifulSoup(data, "html.parser")

      price = str(soup.find("span", {"id": "ref_626307_l"}).contents).replace(",", "").strip("[]").replace("u", "").strip("''")
      change = str(soup.find("span", {"id": "ref_626307_cp"}).contents).replace("+", "").strip("[]").replace("u", "").replace("%", "").strip("''")

      quotes = []
      f = {}
      f['symbol'] = 'SP'
      f['name'] = 'S&P 500'
      f['market_cap'] = ''
      f['price'] = price
      f['change'] = change.strip("()")
      f['date'] = str(dateTime['today'])
      quotes.append(f)

      return quotes

    def recentThreeItems(self):
        SP_price = self.getMarketQuote('INDEXSP:.INX')[0]['price']

        BTC_price = ''
        for coin in self.getCoinPrice():
            if coin['symbol'] == 'BTC':
                BTC_price = coin['price']

        items = {
            "sp_price":SP_price,
            "btc_price":BTC_price
        }

        return items


    def insertSQL(self, array):
        for d in array:
            u = Price(
                            name=d['name'],
                            date = d['date'],
                            symbol = d['symbol'],
                            price = d['price'],
                            change = d['change'],
                            market_cap = d['market_cap']
                           )
            db_session.add(u)
            db_session.commit()
            print d['name'] + ' added!'
        return ''
