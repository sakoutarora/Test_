import json
from solcx import compile_standard, install_solc
import json
from web3 import Web3
install_solc('0.8.0')
with open('Mystorage.sol', 'r') as file:
    smart_con = file.read()
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Mystorage.sol": {"content": smart_con }},
        "settings": {
            "outputSelection": {
                "*" : {
                    "*" : ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] 
                }
            }
        },
    },
    solc_version = "0.8.0",
)
with open('compiled_code.json', 'w') as file:
    json.dump(compiled_sol, file)
