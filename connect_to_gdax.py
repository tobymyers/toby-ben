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
account_id = os.environ.get("ACCOUNT_ID")
sandbox_url = "https://api-public.sandbox.gdax.com"

auth_client = gdax.AuthenticatedClient(api_key, api_secret, passphrase, api_url = "https://api-public.sandbox.gdax.com") #connected to sandbox url for testing
