from vexbi import Base, Response, Client
import mimetypes, urllib
from os.path import basename
import requests

class API(Base):
  def __init__(self, app_id, secret_key):
    client = Client(app_id, secret_key)
    Base.__init__(self, client)

  def create_order(self, order_data):
    return self.post(data=order_data, url=self.url('orders'))

  def delete_order(self, order_id):
    return self.post(data={ 'id': order_id }, url=self.url('order/delete'))

  def clear_all(self, data=None):
    return self.post(data=data, url=self.url('orders/clear'))

  def get_orders(self, market, query={}):
    query = urllib.urlencode(query)
    url = self.url('orders?market={}&{}'.format(market, query))
    return self.get(url=url)

  def get_order(self, order_id):
    return self.get(url=self.url('order?id={}'.format(order_id)))

  def get_account_info(self):
    return self.get(url=self.url('members/me'))

  def get_available_markets(self):
    return self.get(url=self.url('markets'))

  def tickers(self):
    return self.get(url=self.url('tickers'))

  def get_recent_trades(self, market, query={}):
    query = urllib.urlencode(query)
    url = self.url('trades?market={}&{}'.format(market, query))
    return self.get(url=url)

  def my_trades(self, market, query={}):
    query = urllib.urlencode(query)
    url = self.url('trades/my?market={}&{}'.format(market, query))
    return self.get(url=url)
