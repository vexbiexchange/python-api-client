## Vexbi.create_order
### /v2/orders
##### ***POST***

**Summary:** Create a Sell/Buy order.
**Description:** Create a Sell/Buy order.

**Parameters**


| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| market | formData | Unique market id. It's always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'btcusd'. All available markets can be found at /api/v2/markets. | Yes | string |
| side | formData | Either 'sell' or 'buy'. | Yes | string |
| volume | formData | The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 5 btc can be matched with a buy 3 btc order, left 2 btc to be sold; in this case the order's volume would be '5.0', its remaining_volume would be '2.0', its executed volume is '3.0'. | Yes | string |
| price | formData | Price for each unit. e.g. If you want to sell/buy 1 btc at 3000 usd, the price is '3000.0' | No | string |
| ord_type | formData |  | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 | Create a Sell/Buy order. |

## Vexbi.delete_order
### /v2/order/delete
##### ***POST***

**Summary:** Cancel an order.
**Description:** Cancel an order.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | formData | Unique order id. | Yes | integer |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 | Cancel an order. |

## Vexbi.clear_all
### /v2/orders/clear
##### ***POST***

**Summary:** Cancel all my orders.
**Description:** Cancel all my orders.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| side | formData | If present, only sell orders (asks) or buy orders (bids) will be canncelled. | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 | Cancel all my orders. |

## Vexbi.get_orders
### /v2/orders
##### ***GET***

**Summary:** Get your orders, results is paginated.
**Description:** Get your orders, results is paginated.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| market | query | Unique market id. It's always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'btcusd'. All available markets can be found at /api/v2/markets. | Yes | string |
| state | query | Filter order by state, default to 'wait' (active orders). | No | string |
| limit | query | Limit the number of returned orders, default to 100. | No | integer |
| page | query | Specify the page of paginated results. | No | integer |
| order_by | query | If set, returned orders will be sorted in specific order, default to 'asc'. | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get your orders, results is paginated. |

## Vexbi.get_order
### /v2/order
##### ***GET***

**Summary:** Get information of specified order.
**Description:** Get information of specified order.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query | Unique order id. | Yes | integer |

## Vexbi.get_account_info
### /v2/members/me
##### ***GET***

**Summary:** Get your profile and accounts info.
**Description:** Get your profile and accounts info.

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get your profile and accounts info. |

