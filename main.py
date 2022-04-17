from itertools import chain
import json
from web3 import Web3

with open('F:\Defi Web3\compiled_code.json') as file:
    compiled_sol = json.load(file)

bytecodes = compiled_sol['contracts']['Mystorage.sol']['Simple_storae']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['Mystorage.sol']['Simple_storae']['abi']

w3 = Web3(Web3.HTTPProvider('127.0.0.1:8545'))
chain_id = 1337
my_address = '0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1'
private_key = '0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d'
simple_store = w3.eth.contract(abi=abi, bytecode=bytecodes)
nonce = w3.eth.getTransactionCount(my_address)
transaction = simple_store.constructor().buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId":chain_id, "from":my_address, "nonce":nonce})
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# To interact with the contract we need another contract object 
contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(contract.functions.GetFavnumer().call())

print('Chaning fav number of msg.sender to 15 ---- ')
trans = contract.functions.SetFavnumber(15).buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId":chain_id, "from":my_address, "nonce":nonce+1}
)
sign = w3.eth.account.sign_transaction(trans, private_key)
tx_hash = w3.eth.send_raw_transaction(sign.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(contract.functions.GetFavnumer().call())
