
from app import db
import requests
import json
from walletconfig import url
from app.classes.wallet_btc import Btc_WalletAddresses

def getthebalance():

    # standard json header
    headers = {'content-type': 'application/json'}

    # the method/params
    rpc_input = {
        "method": "getbalance",
        "params":
            {
             "minconf": 1,

             }
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "1.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers,
    )

    # the response in json format
    response_json = response.json()
    print(response.json())
    return response_json


def getwalletinfo():

    # standard json header
    headers = {'content-type': 'application/json'}

    # the method/params
    rpc_input = {
        "method": "getwalletinfo",
        "params":
            {
             }
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "1.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers,
    )
    # the response in json format
    response_json = response.json()
    print(response.json())
    return response_json


def listaccounts():

    # standard json header
    headers = {'content-type': 'application/json'}

    # the method/params
    rpc_input = {
        "method": "listaccounts",
        "params":
            {
             }
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "1.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers,
    )

    # the response in json format
    response_json = response.json()
    print(response.json())
    return response_json


if __name__ == '__main__':
    getthebalance()
    getwalletinfo()
    listaccounts()
