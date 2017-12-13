import os
from os.path import join, dirname
from dotenv import load_dotenv
import gdax
import time

#must protect keys for use of public github account
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
passphrase = os.environ.get("PASSPHRASE")
api_secret = os.environ.get("API_SECRET")
api_key = os.environ.get("API_KEY")


#script to connect to gdax
#connected to public client  (not rtm just makes a single call)
# public_client = gdax.PublicClient()
# print(public_client.get_product_ticker(product_id='ETH-USD'))

#connected to websocket feed (lots of data rn)
# wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="BTC-USD")
# wsClient.start()
# while True:
#     print(wsClient.url, wsClient.products)
#     time.sleep(10)

auth_client = gdax.AuthenticatedClient(api_key, api_secret, passphrase)
print(auth_client) #connected and authenticated...gotta do the GITIGNORE stuff immediately

# Use the sandbox API (requires a different set of API access credentials)
sandbox_client = gdax.AuthenticatedClient("4c995ea709a9bce9b677e06a2c6f0e4b", "MsgfX5RU4F1mb7l0jP4nP1kJAWRKVI9k2oBMFX1Jm09DbngtfpO1ZRoK2Ms9yTTh1IWXlFo+bwRxCr/+mffSzw==", "0b9e1dt2ilrp",api_url="https://api-public.sandbox.gdax.com")
print(sandbox_client)


#all these connect!!! time to clean shit up and start building the bot.  Can outsource many things
auth_client.get_accounts()
