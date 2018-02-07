import json
from pprint import pprint

data = json.load(open('test.json'))
txdi = data['op_returns'][0]['txid']

pprint(txdi)