from web3 import Web3
from scan_api import ScanApi
import json


class ERC20Token():
    def __init__(self, token_address, scan_api):
        self.token_address = Web3.to_checksum_address(token_address)

        with open('ScanApi/abis/erc20_token.json') as file:
            self.token_abi = json.load(file)

        self.token_contract = scan_api.rpc.eth.contract(address=self.token_address, abi=self.token_abi)


    def get_token_name(self):
        return self.token_contract.functions.name().call()

    
    def get_token_symbol(self):        
        return self.token_contract.functions.symbol().call()
        

    def get_token_decimals(self):        
        return self.token_contract.functions.decimals().call()
        

    def get_token_total_supply(self):
        return self.token_contract.functions.totalSupply().call()
