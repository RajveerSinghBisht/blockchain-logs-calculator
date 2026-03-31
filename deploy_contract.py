import json
from web3 import Web3
from solcx import compile_source, install_solc

# install Solidity compiler
install_solc('0.8.0')

# connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

account = w3.eth.accounts[0]

# Solidity contract code
contract_source = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LogStorage {
    string[] public hashes;

    function storeHash(string memory hash) public {
        hashes.push(hash);
    }

    function getHash(uint index) public view returns (string memory) {
        return hashes[index];
    }

    function getCount() public view returns (uint) {
        return hashes.length;
    }
}
'''

# compile contract
compiled_sol = compile_source(contract_source, solc_version="0.8.0")
contract_interface = compiled_sol['<stdin>:LogStorage']

# deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

tx_hash = contract.constructor().transact({'from': account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# output
print("Contract deployed at:", tx_receipt.contractAddress)
print("ABI:", contract_interface['abi'])


config = {
    "contract_address": tx_receipt.contractAddress,
    "abi": contract_interface['abi']
}
with open("contract_config.json", "w") as f:
    json.dump(config, f, indent=2)
print("Saved to contract_config.json")