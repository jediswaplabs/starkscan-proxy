from flask import Flask, request
from requests import get
import os

app = Flask(__name__)
SITE_ENV = os.environ.get('SITE_ENV', None)
API_KEY = os.environ.get('API_KEY', None)
if SITE_ENV == "testnet":
  SITE_NAME = 'https://api-testnet.starkscan.co/api/v0/nfts/'
elif SITE_ENV == "mainnet":
  SITE_NAME = 'https://api.starkscan.co/api/v0/nfts/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  contract_address = request.args.get('contract_address')
  owner_address = request.args.get('owner_address')

  return get(f'{SITE_NAME}{path}', params = {"contract_address": contract_address, "owner_address": owner_address}, headers = {"X-API-KEY": API_KEY}).content

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)