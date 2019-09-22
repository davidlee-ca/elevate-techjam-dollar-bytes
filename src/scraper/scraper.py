import requests
import json
import os
import sys
from time import sleep

api_key = os.getenv('TD_DAVINCI_API_KEY')
segment = sys.argv[1]
acct_path, acct_prefix = "accounts/", "acct_"
tx_path, tx_prefix = "transactions/", "tx_"
customer_id_file = f"customerid_{segment}.txt"

def get_customer_ids(customer_id_file):
    # get a list of customer ID
    cids = []
    with(open(customer_id_file)) as f:
        line = f.readline()
        while line:
            cids.append(line.strip())
            line = f.readline()
    return cids


def get_accounts(cid):
    print(f"Requesting accounts for #{cid}...")
    try:
        retry = 0
        response = requests.get(f"https://api.td-davinci.com/api/customers/{cid}/accounts",
                                headers = { 'Authorization': api_key } )
        while response.status_code != 200 and retry < 3:
            retry += 1
            sleep(1)
            response = requests.get(f"https://api.td-davinci.com/api/customers/{cid}/accounts",
                                    headers = { 'Authorization': api_key } )
        response_data = response.json()
        filename = acct_path + acct_prefix + cid + '.json'
        with(open(filename, 'w')) as fw:
            json.dump(response_data, fw)
    except:
        print(f"ERROR: failed to fetch account information for {cid}")


def get_transactions(cid):
    print(f"Requesting transactions for #{cid}...")
    try:
        retry = 0
        response = requests.get(f"https://api.td-davinci.com/api/customers/{cid}/transactions",
                                headers = { 'Authorization': api_key } )
        while response.status_code != 200 and retry < 3:
            retry += 1
            sleep(1)
            response = requests.get(f"https://api.td-davinci.com/api/customers/{cid}/transactions",
                                    headers = { 'Authorization': api_key } )
        response_data = response.json()
        filename = tx_path + tx_prefix + cid + '.json'
        with(open(filename, 'w')) as fw:
            json.dump(response_data, fw)
    except:
        print(f"ERROR: failed to fetch transactions information for {cid}")


if __name__ == "__main__":
    cids = get_customer_ids(customer_id_file)
    count = 0
    for customer in cids:
        count += 1
        if count % 500 == 0:
            print(f"=== Processing record {count} of {len(cids)}")
        get_accounts(customer)
        get_transactions(customer)
