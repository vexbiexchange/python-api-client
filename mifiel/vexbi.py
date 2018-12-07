from mifiel import Base, Response, Client
import mimetypes, urllib
from os.path import basename
import requests

class Vexbi(Base):
  def __init__(self, app_id, secret_key):
    client = Client(app_id, secret_key)
    Base.__init__(self, client)

  def create_order(self, order_data):
    self.post(data=order_data, url=self.url('orders'))

  def delete_order(self, order_id):
    self.post(data={ 'id': order_id }, url=self.url('order/delete'))

  def clear_all(self, data=None):
    self.post(data=data, url=self.url('orders/clear'))

  def get_orders(self, market, query={}):
    query = urllib.urlencode(query)
    url = self.url('orders?market={}&{}'.format(market, query))
    self.get(url=url)

  def get_account_info(self):
    self.get(url=self.url('members/me'))

  def get_available_markets(self):
    self.get(url=self.url('markets'))

  def tickers(self):
    self.get(url=self.url('tickers'))
