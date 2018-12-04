from mifiel import Response
import requests

class Base(object):
  def __init__(self, client):
    object.__setattr__(self, 'sandbox', False)
    object.__setattr__(self, 'client', client)
    object.__setattr__(self, 'response', Response())
    # initialize id
    self.id = None

  def save(self):
    if self.id is None:
      return False
    self.process_request('put', url=self.url(self.id), data=self.get_data())

  def url(self, path=None):
    return self.client.url().format(path=path)

  def execute_request(self, method, url=None, data=None, json=None):
    if not url:
      url = self.url()

    if method == 'post':
      response = requests.post(
        url=url,
        auth=self.client.auth,
        data=data,
        json=json
      )
    elif method == 'put':
      response = requests.put(url, auth=self.client.auth, json=data)
    elif method == 'get':
      response = requests.get(url, auth=self.client.auth, json=data)
    elif method == 'delete':
      response = requests.delete(url, auth=self.client.auth, json=data)

    return response

  def process_request(self, method, url=None, data=None, json=None):
    response = self.execute_request(method, url, data, json)
    self.set_data(response)

  def set_data(self, response):
    self.response.set_response(response)

  def get_data(self):
    return self.response.get_response()

  def __setattr__(self, name, value):
    self.response.set(name, value)

  def __getattr__(self, name):
    return self.response.get(name)
