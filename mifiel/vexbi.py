from mifiel import Base, Response
import mimetypes
from os.path import basename
import requests

class Vexbi(Base):
  def __init__(self, client):
    Base.__init__(self, client)

  @staticmethod
  def get_account_info(client):
    vex = Vexbi(client)
    vex.process_request('get', url=vex.url('members/me'))
    return vex

  @staticmethod
  def get_available_markets(client):
    vex = Vexbi(client)
    vex.process_request('get', url=vex.url('markets'))
    return vex

  @staticmethod
  def tickers(client):
    vex = Vexbi(client)
    vex.process_request('get', url=vex.url('tickers'))
    return vex

