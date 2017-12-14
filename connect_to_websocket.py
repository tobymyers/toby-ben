#connect to websocket
connected to websocket feed (lots of data rn)
wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="BTC-USD")
wsClient.start()
while True:
    print(wsClient.url, wsClient.products)
    time.sleep(10)
