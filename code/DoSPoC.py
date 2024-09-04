import sys
import time
import concurrent.futures
from web3 import Web3
import secrets
import random
from eth_account import Account
from queue import Queue

def generate_high_entropy_data_secrets(size):
    return secrets.token_bytes(size)

def send_transaction(web3, my_address, private_key, to_address, value_ether, chain_id, input_data):
    try:
        input_data = '0x' + input_data.hex()
        transaction = {
            'to': to_address,
            'value': web3.to_wei(value_ether, 'ether'),
            'chainId': chain_id,
            'data': input_data
        }
        transaction['gas'] = int(web3.eth.estimate_gas(transaction) * 1.1)

        def send_and_wait():
            transaction['nonce'] = web3.eth.get_transaction_count(my_address)
            transaction['gasPrice'] = int(web3.eth.gas_price * 1.5)
            signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"Transaction sent successfully, transaction hash: {web3.to_hex(tx_hash)}")
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt

        while True:
            try:
                receipt = send_and_wait()
                if receipt.status == 1:
                    print("Transaction succeeded")
                    return 1
                else:
                    print("Transaction failed")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Retrying...")

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def replace_with_zeros(byte_array, num_zeros):
    original_length = len(byte_array)
    
    if num_zeros > original_length:
        raise ValueError("Number of zeros to replace exceeds the length of the byte array")
    
    new_byte_array = bytearray(byte_array)
    replace_positions = random.sample(range(original_length), num_zeros)
    
    for pos in replace_positions:
        new_byte_array[pos] = 0
    
    return bytes(new_byte_array)

def generate_ethereum_address():
    account = Account.create()
    private_key = account.key.hex()
    address = account.address
    return address, private_key

def send_transaction_thread(web3, my_address, private_key, value_ether, chain_id, payload):
    try:
        to_address = generate_ethereum_address()[0]
        cresult = send_transaction(web3, my_address, private_key, to_address, value_ether, chain_id, payload)
        print(f"Transaction result: {cresult}")
    except Exception as e:
        print(f"An error occurred in thread: {e}")

def worker(web3, my_address, private_key, value_ether, chain_id, q):
    while True:
        j, i, payload = q.get()
        if payload is None:
            break
        send_transaction_thread(web3, my_address, private_key, value_ether, chain_id, payload)
        print(j, i, "successfully finished")
        q.task_done()

def main():

    local_node_url = "http://127.0.0.1:8545"
    web3 = Web3(Web3.HTTPProvider(local_node_url))

    if web3.is_connected():
        print("Connected to node")
    else:
        print("Failed to connect to node")
        sys.exit(1)

    # address and private keys
    addresses_private_keys = [
        ("", ""),
        ("", ""),
        ("", ""),
        ("", "")
    ]


    num_addresses = len(addresses_private_keys)
    num_threads = num_addresses

    value_ether = 1e-18
    chain_id = 17000
    maxlen_calldata = 130859

    print("hit1")
    queues = [Queue() for _ in range(num_threads)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for idx in range(num_threads):
            my_address, private_key = addresses_private_keys[idx % num_addresses]
            executor.submit(worker, web3, my_address, private_key, value_ether, chain_id, queues[idx])
        print("hit2")
        for j in range(0, 1000):
            for i in range(0, 23):
                seed = generate_high_entropy_data_secrets(maxlen_calldata)
                payload = replace_with_zeros(seed, 67173)
                
                if i == 22:
                    payload = payload[:int(maxlen_calldata * 0.97)]
                
                q_idx = i % len(queues)
                queues[q_idx].put((j, i, payload))

        for q in queues:
            q.join()

        for q in queues:
            q.put((None, None, None))

if __name__ == "__main__":
    main()
