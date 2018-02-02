from binance.client import Client
from Utilities import Utilities
from datetime import datetime

from sqlalchemy.sql import select

util = Utilities()

class MarketTrade:
    def __init__(self):
        pass

    def getClient(self):

        api_key = util.binanceKey()['key']
        api_secret = util.binanceKey()['secret']

        client = Client(api_key, api_secret)

        return client


    def getAllStocks(self):
        prices = self.getClient().get_all_tickers()
        depth = self.getClient().get_order_book(symbol='BNBBTC')
        return depth

    def getAccountInfo(self):
        info = self.getClient().get_account()
        # status = self.getClient().get_account_status()

        test = {
            "info":info
            # "status":status
        }
        return test


    def marketOrder(self):
        return ''
