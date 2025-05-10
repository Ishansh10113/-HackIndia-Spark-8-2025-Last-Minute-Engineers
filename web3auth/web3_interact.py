from web3 import Web3
import json
import os
from decouple import config

# Load .env values
WEB3_RPC = config('WEB3_RPC')
PRIVATE_KEY = config('PRIVATE_KEY')
CONTRACT_ADDRESS = Web3.to_checksum_address(config('CONTRACT_ADDRESS'))
MY_ADDRESS = Web3.to_checksum_address("0x5F8BEbB4bB449Ca33eab226A689B341343024EDD")  # your wallet

# Connect to Alchemy or Ganache
w3 = Web3(Web3.HTTPProvider(WEB3_RPC))

# Load ABI
abi_path = os.path.join(os.path.dirname(__file__), "contract_abi.json")
with open(abi_path) as f:
    abi = json.load(f)

# Get contract instance
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

# Function to submit a startup
def submit_startup(name, idea, funding_required):
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    txn = contract.functions.submitStartup(name, idea, funding_required).build_transaction({
        'from': MY_ADDRESS,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.to_wei('20', 'gwei')
    })

    signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return tx_hash.hex()
