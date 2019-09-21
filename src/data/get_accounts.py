import grequests  
import json
import os

customer_id_file = "cids.txt"
api_key = os.getenv('TD_DAVINCI_API_KEY')
destination_file_prefix = "accounts/accounts_"
cids = []

# get a list of customer ID
with(open(customer_id_file)) as f:
    line = f.readline()
    while line:
        cids.append(line.strip())
        line = f.readline()

urls = (f"https://api.td-davinci.com/api/customers/{cid}/accounts" for cid in cids)
rs = (grequests.get(u, headers={'Authorization': api_key}) for u in urls)
accounts = grequests.map(rs)

for cid, account in zip(cids, accounts):
    accounts_data = account.json()
    accounts_filename = destination_file_prefix + cid + ".json"
    with(open(accounts_filename, 'w')) as fw:
        json.dump(accounts_data, fw)
