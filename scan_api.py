import requests
from web3 import Web3


class ScanApi:
    def __init__(self, rpc, chain:str, api_key:str):
        """_summary_

        Args:
            rpc (_type_): rpc url to connect with the blockchain
            chain (str): It is the chain name. Options supported: 
            ETH -> etherscan
            BSC -> bscscan
            BASE -> basescan
            MATIC -> polygonscan
            api_key (str): In each of the scans mentioned above, the platform provide to you an api key
        """
        self.rpc = rpc
        self.chain = chain.upper()
        self.api_key = api_key
        self.standard_url = ''

        if self.chain=='ETH' or self.chain=='ETHEREUM':
            self.standard_url = 'https://api.etherscan.io/api'
        elif self.chain=='BSC': 
            self.standard_url = 'https://api.bscscan.com/api'
        elif self.chain=='MATIC':
            self.standard_url = 'https://api.polygonscan.com/api'
        elif self.chain=='BASE':
            self.standard_url = 'https://api.basescan.org/api'
        elif self.chain=='ARBITRUM' or self.chain=='ARB':
            self.standard_url = 'https://api.arbiscan.io/api'
        else:
            raise ValueError('Chain name invalid')


    def get_native_token_balance(self, account_address):
        url = f"{self.standard_url}?module=account&action=balance&address={account_address}&apikey={self.api_key}"
        try:
            response = requests.get(url)
        except Exception as e:
            print(f'Falha ao se conectar com a API da {self.chain}')
            print(e)
        else:
            data = response.json()
            return data['result']

    
    def get_native_token_balance_for_multiple_addresses(self, *args):
        for address in args:
            address_parameter = 'saber como usar o join' # AQUUUUI
        url = f"{self.standard_url}?module=account&action=balancemulti&address={args}&tag=latest&apikey={self.api_key}"


    def get_a_list_of_normal_transactions_by_address(self, address, start_block, end_block):
        pass
        

    def get_contract_abi(self, contract_address):
        url = f'{self.standard_url}?module=contract&action=getabi&address={contract_address}&apikey={self.api_key}'
        try:
            response = requests.get(url)
        except Exception as e:
            print(f'Falha ao se conectar com a API da {self.chain}')
            print(e)
        else:
            data = response.json()
            try:
                return data['result']
            except:
                return 'Falha ao pegar abi do contrato'


    def number_of_transactions_found(self, account_address, start_block=0, end_block=99999999, page=1, offset=1000, sort='asc'):
        url = f'{self.standard_url}?module=account&action=txlist&address={account_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort={sort}&apikey={self.api_key}'
        try:
            response = requests.get(url)
        except Exception as e:
            print(f'Falha ao se conectar com a API da {self.chain}')
            print(e)
        else:
            data = response.json()
            list_transactions = data['result']
            quantity = 0
            for _ in list_transactions:
                quantity+=1
            return quantity


    def get_tokens_transfers(self, address:str, start_block:int=0, end_block:int=99999999, page:int=1, offset:int=1000, sort:str='asc'):
        all_transactions = []
        API_URL = f'{self.standard_url}?module=account&action=tokentx&'
        
        while True:
            params = {
                "address": address,
                "startBlock": start_block,
                "endBlock": end_block,
                "page": page,
                "offset": offset,
                "sort": sort,
                "apikey": self.api_key
            }
            try:
                response = requests.get(API_URL, params=params)
            except Exception as e:
                print('Falha ao se conectar com a API da {self.chain}')
                print(e)
            else:
                data = response.json()  
                list_transactions = data['result']

                if not list_transactions:
                    break  
               
                all_transactions.append(list_transactions)
                page+=1
        return all_transactions


    def get_first_transaction_block(self, wallet_address):
        url = f"{self.standard_url}?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&page=1&offset=1&sort=asc&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "1" and data["result"]:
            first_transaction = data["result"][0]
            return first_transaction["blockNumber"]
        else:
            return "Nenhuma transação encontrada para esta carteira."
    

    def get_block_number_by_timestamp(self, timestamp, closest):
        url = f'{self.standard_url}?module=block&action=getblocknobytime&timestamp={timestamp}&closest={closest}&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        
        return int(data['result'])
        

    def get_transactions(self, account_address, start_block=0, end_block=99999999):
        page = 1
        offset = 1000  # Quantidade de transações por página
        while True:
            url = f'{self.standard_url}?module=account&action=txlist&address={account_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort=asc&apikey={self.api_key}'
            response = requests.get(url)
            data = response.json()
            transactions = data['result']

            if not transactions:
                break  # Não há mais transações, sair do loop

            for transaction in transactions:
                yield transaction

            page += 1  # Incrementar a página para a próxima chamada


    def get_logs(self, address, topic0, start_block=0, end_block=99999999):
        url = f'{self.standard_url}?module=logs&action=getLogs&fromBlock={start_block}&toBlock={end_block}&address={address}&topic0={topic0}&apikey={self.api_key}'
        try:
            response = requests.get(url)
        except:
            print('Error when tried to get logs')
        else:
            data = response.json()
            return data['result']


    def get_logs_filtered(self, address, topic0, topic1, start_block=0, end_block=99999999):
        url = f'{self.standard_url}?module=logs&action=getLogs&fromBlock={start_block}&toBlock={end_block}&address={address}&topic0={topic0}&topic0_1_opr=and&topic1={topic1}&apikey={self.api_key}'
        try:
            response = requests.get(url)
        except:
            print('Error when tried to get logs')
        else:
            data = response.json()
            return data['result']


    def get_input_decoded(self, contract_address, input_data):
        contract_address = Web3.to_checksum_address(contract_address)
        abi = self.get_contract_abi(contract_address)
        contract = self.rpc.eth.contract(address=contract_address, abi=abi)
        return contract.decode_function_input(input_data) # it's a tuple with the method name and the arguments used
    

    def get_timestamp(self, tx_hash):
        try:
            tx = self.rpc.eth.get_transaction(tx_hash)
        except:
            print(f'Erro ao pegar a transação. Hash informado foi {tx_hash}. Verifique novamente.')
        else:
            return self.rpc.eth.get_block(tx['blockNumber'])['timestamp']
        
    
    def get_contract(self, contract_address, abi):
        contract_address = Web3.to_checksum_address(contract_address)
        return self.rpc.eth.contract(address=contract_address, abi=abi)
    

    def get_token_name(self, token_address):
        token_contract_address = Web3.to_checksum_address(token_address)
        abi = [{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]
        token_contract = self.rpc.eth.contract(address=token_contract_address, abi=abi)
        
        return token_contract.functions.name().call()


    
    def get_token_symbol(self, token_address):
        token_contract_address = Web3.to_checksum_address(token_address)
        abi = [{'constant': True, 'inputs': [], 'name': 'symbol', 'outputs': [{'name': '', 'type': 'string'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}]
        token_contract = self.rpc.eth.contract(address=token_contract_address, abi=abi)
        
        return token_contract.functions.symbol().call()
        
    

    def get_token_decimals(self, token_address):
        token_contract_address = Web3.to_checksum_address(token_address)
        abi = [{'constant': True, 'inputs': [], 'name': 'decimals', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}]
        token_contract = self.rpc.eth.contract(address=token_contract_address, abi=abi)
        
        return token_contract.functions.decimals().call()
        

    def get_token_total_supply(self, token_address):
        token_contract_address = Web3.to_checksum_address(token_address)
        abi = [{'constant': True, 'inputs': [], 'name': 'totalSupply', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}]
        token_contract = self.rpc.eth.contract(address=token_contract_address, abi=abi)

        return token_contract.functions.totalSupply().call()

