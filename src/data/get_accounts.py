import grequests  
import json
import os
import sys
from itertools import chain

api_key = os.getenv('TD_DAVINCI_API_KEY')
segment = sys.argv[1]
destination_file_prefix = f"accounts_{segment}/accounts_"
customer_id_file = f"customers_{segment}.txt"
zfill_padding = 5


def get_customer_ids(customer_id_file):
    # get a list of customer ID
    cids = []
    with(open(customer_id_file)) as f:
        line = f.readline()
        while line:
            cids.append(line.strip())
            line = f.readline()
    return cids


def cids_in_chunks(cids, size=500):
    # chunkify the customer IDs
    starting_index, count = 0, 1
    while starting_index < len(cids):
        yield count, cids[starting_index:starting_index+size]
        starting_index += size
        count += 1


def get_accounts(count, cids):
    # grab the bank accounts and consolidate
    urls = (f"https://api.td-davinci.com/api/customers/{cid}/accounts" for cid in cids)
    rs = (grequests.get(u, headers={'Authorization': api_key}) for u in urls)
    accounts = grequests.map(rs)
    accounts_data = [acct.json() for acct in accounts]
    bank_accounts = list(chain.from_iterable(acct['result']['bankAccounts'] for acct in accounts_data))
    
    filename = destination_file_prefix + str(count).zfill(zfill_padding) + '.json'
    with(open(filename, 'w')) as fw:
        json.dump(bank_accounts, fw)


if __name__ == "__main__":
    cids = get_customer_ids(customer_id_file)

    for count, customers in cids_in_chunks(cids, 500):
        print(f"Starting bin {count}")
        get_accounts(count, customers)
