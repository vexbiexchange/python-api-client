import responses
from vexbi import API

class TestAPI:

  def setUp(self):
    self.api = API('test_api', 'test_secret_key')

  def test_use_sandbox(self):
    assert self.api.client.sandbox == False
    self.api.use_sandbox()
    assert self.api.client.sandbox == True, 'sandbox must True'

  @responses.activate
  def test_create_order(self):
    responses.add(responses.POST, self.api.url('orders'), json={ "message": "order created" }, status=200)
    response = self.api.create_order({})
    assert response == { "message": "order created" }

  @responses.activate
  def test_delete_order(self):
    responses.add(responses.POST, self.api.url('order/delete'), json={ "message": "order canceled" }, status=200)
    response = self.api.delete_order(1)
    assert response == { "message": "order canceled" }

  @responses.activate
  def test_clear_all(self):
    responses.add(responses.POST, self.api.url('orders/clear'), json={ "message": "all orders canceled" }, status=200)
    response = self.api.clear_all({})
    assert response == { "message": "all orders canceled" }

  @responses.activate
  def test_get_orders(self):
    responses.add(responses.GET, self.api.url('orders?market=btcmxn'), json={ "orders": { "id": 1 } }, status=200)
    response = self.api.get_orders('btcmxn', {})
    assert response == { "orders": { "id": 1 } }

  @responses.activate
  def test_get_order(self):
    responses.add(responses.GET, self.api.url('order?id=1'), json={ "order": { "id": 1 } }, status=200)
    response = self.api.get_order(1)
    assert response == { "order": { "id": 1 } }

  @responses.activate
  def test_get_account_info(self):
    responses.add(responses.GET, self.api.url('members/me'), json={ "member": { "id": 1 } }, status=200)
    response = self.api.get_account_info()
    assert response == { "member": { "id": 1 } }

  @responses.activate
  def test_get_available_markets(self):
    responses.add(responses.GET, self.api.url('markets'), json={ "markets": { "id": 1 } }, status=200)
    response = self.api.get_available_markets()
    assert response == { "markets": { "id": 1 } }

