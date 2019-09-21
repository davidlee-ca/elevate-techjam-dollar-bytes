import requests
import json
import os

zfill_padding = 5
maximum_number_of_requests = 1500
api_key = os.getenv('TD_DAVINCI_API_KEY')
destination_file_prefix = "customers/customers_"
continuation_key = str()

for i in range(maximum_number_of_requests):
    print(f"Getting request #{i+1}...")

    response = requests.post('https://api.td-davinci.com/api/raw-customer-data',
        headers = { 'Authorization': api_key },
        json={ 'continuationToken': continuation_key } )
    response_data = response.json()
    print(response)

    filename = destination_file_prefix + str(i).zfill(zfill_padding) + '.json'
    with(open(filename, 'w')) as w:
        json.dump(response_data, w)

    # Finish 
    if 'continuationToken' in response_data['result']:
        continuation_key = response_data['result']['continuationToken']
        print(f"Continuation key: {continuation_key}")
    else:
        print("No continuation key found! Exiting...")
        break
