from .api_auth import RequestsApiAuth

class Client:
  def __init__(self, app_id, secret_key):
    self.sandbox = False
    self.auth = RequestsApiAuth(app_id, secret_key)
    self.base_url = 'https://www.vexbi.com'

  def use_sandbox(self):
    self.sandbox = True
    self.base_url = 'https://sandbox.vexbi.com'

  def set_base_url(self, base_url):
    self.base_url = base_url

  def url(self):
    return self.base_url + '/api/v2/{path}'
