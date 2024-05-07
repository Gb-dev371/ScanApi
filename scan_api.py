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
        self.chain = chain
        self.api_key = api_key
        self.standard_url = ''

        if chain=='ETH':
            self.standard_url = 'https://api.etherscan.io/api'
        elif chain=='BSC': 
            self.standard_url = 'https://api.bscscan.com/api'
        elif chain=='MATIC':
            self.standard_url = 'https://api.polygonscan.com/api'
        elif chain=='BASE':
            self.standard_url = 'https://api.basescan.org/api'


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


    def get_a_list_of_normal_transactions_by_address(self, address, start_block, end_block, api_key):
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
        # first_block = int(get_first_transaction_block(address))
        # current_block = bsc.eth.get_block('latest')
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
    

# def number_of_tokens_transfers_found(list_transactions):
#     quantity = 0
#     for tx in list_transactions:
#         quantity+=1
#     return quantity


    def get_first_transaction_block(self, wallet_address):
        url = f"{self.standard_url}?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&page=1&offset=1&sort=asc&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "1" and data["result"]:
            first_transaction = data["result"][0]
            return first_transaction["blockNumber"]
        else:
            return "Nenhuma transação encontrada para esta carteira."


# def get_normal_transactions(self, account_address):
#     # url = f'https://api.{self.chain}.com/api?module=account&action=txlist&address={account_address}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={API_KEY_BINANCE_SCAN}'
#     # response = requests.get(url)
#     # data = response.json()
#     # return data['result']

#     all_transactions = []
#     page=1
#     API_URL = f'https://api.{self.chain}.com/api?module=account&action=txlist&'
#     first_block = int(get_first_transaction_block(account_address))
#     chain = self.chain
#     current_block = chain.eth.get_block('latest')

#     while True:
#         params = {
#             "address": account_address,
#             "startBlock": first_block,
#             "endBlock": current_block,
#             "page": page,
#             "offset": 1000,
#             "sort": "asc",
#             "apikey": self.api_key
#             # Adicione outros parâmetros conforme necessário
#         }
#         response = requests.get(API_URL, params=params)
#         data = response.json()  # Ajuste de acordo com o formato da resposta
#         list_transactions = data['result']

#         if not list_transactions:
#             # print(all_transactions[-1][-1])
#             timestamp = int(all_transactions[-1][-1]['timeStamp'])
#             print(f"Last transaction found: {timestamp_to_date(timestamp)}")
#             print('finished')
#             break  # Encerra o loop se não houver mais transações

        

#         all_transactions.append(list_transactions)
#         # print(list_transactions)
#         page += 1  # Incrementa a página para a próxima chamada
#     # print(type(all_transactions))
#     return all_transactions
# #Nonetypeerror por conta do page e offset


# def get_token_transfer_filtered(self, token_address, account_address, start_block=0, end_block=99999999, page=1):
#     url = f'https://api.{self.chain}.com/api?module=account&action=tokentx'

#     while True:
#         params = {
#             'contractaddress':token_address,
#             'address':account_address,
#             'page':page,
#             'offset':1000,
#             'startblock':0,
#             'endblock':999999999,
#             'sort':'asc',
#             'apikey':self.api_key,
#         }
#         response = requests.get(url, params=params)
#         data = response.json() 
#         list_transactions = data['result']

#         if not list_transactions:
#             print('finished')
#             break  # Encerra o loop se não houver mais transações

#         page+=1
#         yield list_transactions


# def get_function_name_used_filtered(contract_address, account_address):
#     list_transactions = get_token_transfer_filtered(contract_address, account_address)
#     for tx in list_transactions:
#         print(tx['functionName'])


# def get_transactions_by_name_method(self, address, method):
#     url = f'https://api.{self.chain}.com/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={API_KEY_BINANCE_SCAN}'
#     response = requests.get(url)
#     data = response.json()
#     # list_transactions = []
#     for tx in data['result']:
#         print(tx)
#         if tx['functionName'] == method:
#             yield tx
#         # list_transactions.append(tx)
#     # return list_transactions
        

# def pool_tracker(self, pool_address, contract_address, account_address, start_block, end_block, api_key, coin):
#     pool_address = pool_address.lower()
#     contract_address = contract_address.lower()
#     account_address = account_address.lower()

#     url = f'https://api.{self.chain}.com/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&startblock={start_block}&endblock={end_block}&page=1&offset=500&sort=asc&apikey={api_key}'

#     response = requests.get(url)
#     data = response.json()
#     response = data['result']
#     transactions_list = []

#     quantity_tx = 0
#     hash = []
#     from_tx = []
#     to_tx = []
#     amount_withdraw = []
#     amount_deposited = []

#     for transaction_info in response:
#         # print(transaction_info)
#         from_tx = transaction_info['from']
#         to_tx = transaction_info['to']
#         value = transaction_info['value']
#         # print(from_tx)
#         # print(to_tx)


#         if from_tx == pool_address:
#             value = int(value)
#             if coin == 'BRZ':
#                 amount_withdraw.append(convert_4(value))
#                 print(f'Transfero sacou {format(convert_4(value))} {coin} da pool')
#             elif coin == 'jBRL':
#                 amount_withdraw.append(convert_18(value))
#                 print(f'Transfero sacou {format(convert_18(value))} {coin} da pool')

#         elif to_tx == pool_address:
#             value = int(value)
#             if coin == 'BRZ':
#                 amount_deposited.append(convert_4(value))
#                 print(f'Transfero depositou {format(convert_4(value))} {coin} da pool')
#             elif coin == 'jBRL':
#                 amount_deposited.append(convert_18(value))
#                 print(f'Transfero depositou {format(convert_18(value))} {coin} da pool')


#     amount = sum(amount_deposited) - sum(amount_withdraw)
#     print(f"Restante: {format(amount)} {coin}")


    def get_block_number_by_timestamp(self, timestamp, closest):
        url = f'{self.standard_url}?module=block&action=getblocknobytime&timestamp={timestamp}&closest={closest}&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        
        return int(data['result'])
        

# def get_log_decoded_swap(self, contract_address, log):
#     contract_address = Web3.to_checksum_address(contract_address)
#     abi = get_contract_abi(contract_address)
#     contract = self.rpc.eth.contract(address=contract_address, abi=abi)
#     decoded_log = contract.events.Swap().process_log(log)
#     return decoded_log

# def get_token_and_amount_used_in_transaction(input_decoded):
#     # print('getting token and amount')
#     return input_decoded[1]['_incentive'], input_decoded[1]['_amount']


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


# def erc721_get_id(self, contract_address, account_address):
#     contract_address = contract_address.lower()
#     account_address = account_address.lower()
#     url = f'https://api.{self.chain}.com/api?module=account&action=tokennfttx&contractaddress={contract_address}&address={account_address}&startblock=0&endblock=99999999&page=1&offset=100&sort=asc&apikey={API_KEY_BINANCE_SCAN}'
#     response = requests.get(url)
#     data = response.json()
#     result = data['result']

#     quantity_tx = 0
#     nfts_ids = []

#     for transaction_info in result:
#         quantity_tx+=1
#         id = int(transaction_info['tokenID'])
#         nfts_ids.append(id)
#         # print(transaction_info)

#     # print(f'Foram encontradas {quantity_tx} nfts')
#     # print(nfts_ids)
        
#     return nfts_ids


    def get_logs(self, address, topic0, start_block=0, end_block=99999999):
        url = f'{self.standard_url}?module=logs&action=getLogs&fromBlock={start_block}&toBlock={end_block}&address={address}&topic0={topic0}&apikey={self.api_key}'
        try:
            response = requests.get(url)
        except:
            print('Erro ao pegar os logs')
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

    
    def get_token_symbol(self, token_address, token_abi):
        token_contract_address = Web3.to_checksum_address(token_address)
        token_contract = self.rpc.eth.contract(address=token_contract_address, abi=token_abi)
        
        try:
            return token_contract.functions.symbol().call()
        except:
            return 'Error'
    

    def get_token_decimals(self, token_address, token_abi):
        token_contract_address = Web3.to_checksum_address(token_address)
        token_contract = self.rpc.eth.contract(address=token_contract_address, abi=token_abi)
        
        try:
            return token_contract.functions.decimals().call()
        except:
            return 'Error'


# def get_logs_filtered(self, address, topic0, topic1, start_block=0, end_block=99999999):
#     url = f'https://api.{self.chain}.com/api?module=logs&action=getLogs&fromBlock={start_block}&toBlock={end_block}&address={address}&topic0={topic0}&topic0_1_opr=and&topic1={topic1}&apikey={API_KEY_BINANCE_SCAN}'
#     try:
#         response = requests.get(url)
#     except:
#         print('Erro ao pegar os logs')
#     else:
#         data = response.json()
#         return data['result']
