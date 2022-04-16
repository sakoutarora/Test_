import json
from web3 import Web3

with open('F:\Defi Web3\compiled_code.json') as file:
    compiled_sol = json.load(file)

bytecodes = compiled_sol['contracts']['Mystorage.sol']['Simple_storae']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['Mystorage.sol']['Simple_storae']['abi']

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
chain_id = 5777
my_address = '0xb77Ca4F10A6d28dbCfb87B9fbfA5A1b99328D67F'
private_key = '0xf0c972ca1d2bfa22e4d0e08967c507cf458d3017f8b34260f4b2e54b6aa54198'
simple_store = w3.eth.contract(abi=abi, bytecode=bytecodes)
print(w3.eth.get_block('latest'))