import requests
import json
import ast

rpc_ip = '95.217.130.11'  # your RPC server IP
rpc_port = 4000  # default RPC port
rpc_base_url = "http://" + rpc_ip + ":" + str(rpc_port) + "/"

rpc_base_struct = {
    "jsonrpc": "2.0",
    "method": "",
    "params": {},
    "id": ""
}

def handleStruct(method, params, request_identifier):
    rpc_handle_struct = rpc_base_struct
    rpc_handle_struct['method'] = method
    rpc_handle_struct['params'] = params
    rpc_handle_struct['id'] = request_identifier
    response = requests.post(rpc_base_url, json=rpc_handle_struct)
    print(response.content.decode('utf-8'))
    if response.status_code == 200:
        return [True, ast.literal_eval(response.content.decode('utf-8'))]
    else:
        return [False, False]

def methodInfo(request_identifier):
    params = {}
    res = handleStruct('info', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

# address_type : identifier OR nyzo_string
def methodBalance(request_identifier, address_type, typed_address):
    params = {address_type: typed_address}
    res = handleStruct('balance', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

def methodAllTransactionsPool(request_identifier):
    params = {}
    res = handleStruct('alltransactions', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

def methodGetTransactionPool(block_height, request_identifier):
    params = {'height': block_height}
    res = handleStruct('gettransaction', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

def methodBroadcastSignature(hex_signature, request_identifier):
    params = {'tx': hex_signature}
    res = handleStruct('broadcast', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

# address_type = private_seed / private_nyzo_string
def methodRawTransaction(request_identifier, amount, address_type, typed_receiver, typed_sender, typed_private_key, sender_data, broadcast=True, timestamp=None, signature=None):
    if address_type == 'private_seed':
        recv_handled = 'receiver_identifier'
        sendr_handled = 'sender_identifier'
    elif address_type == 'private_nyzo_string':
        recv_handled = 'receiver_nyzo_string'
        sendr_handled = 'sender_nyzo_string'
    else:
        print('error - address_type invalid')
        return False

    params = {
        address_type: typed_private_key,
        recv_handled: typed_receiver,
        sendr_handled: typed_sender,
        'sender_data': sender_data,
        'broadcast': broadcast,
        'amount': amount
    }

    if timestamp is not None:
        params['timestamp'] = timestamp

    if signature is not None:
        params['signature'] = signature

    res = handleStruct('rawtransaction', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        print(res)
        return False

def methodTransactionConfirmed(request_identifier, tx_signature):
    params = {'tx': tx_signature}
    res = handleStruct('transactionconfirmed', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

def methodCycleInfo(request_identifier):
    params = {}
    res = handleStruct('cycleinfo', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

def methodBlockInfo(request_identifier, block_height):
    params = {
        'height': block_height
    }
    res = handleStruct('block', params, request_identifier)
    if res[0]:
        print('success')
        return res[1]
    else:
        print('error')
        return False

# example
d = methodRawTransaction('tx01', 901, 'private_nyzo_string', 'id__receiver', 'id__sender', 'key_', '', broadcast=True, timestamp=None, signature=None)
if d:
    methodBroadcastSignature(d, 'tx02')

