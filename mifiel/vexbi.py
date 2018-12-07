from mifiel import Base, Response, Client
import mimetypes, urllib
from os.path import basename
import requests

class Vexbi(Base):
  def __init__(self, app_id, secret_key):
    client = Client(app_id, secret_key)
    Base.__init__(self, client)

  def get_account_info(self):
    self.get(url=self.url('members/me'))

  def get_available_markets(self):
    self.get(url=self.url('markets'))

  def tickers(self):
    self.get(url=self.url('tickers'))
