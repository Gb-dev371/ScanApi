from scan_api import ScanApi
from dotenv import load_dotenv
import os 
from web3 import Web3 

load_dotenv(override=True)
API_KEY_BINANCE_SCAN = os.getenv('BINANCE_SCAN_API_KEY')
API_KEY_POLYGON_SCAN = os.getenv('POLYGON_SCAN_API_KEY')
API_KEY_INFURA = os.getenv('INFURA_API_KEY')

pol = Web3(Web3.HTTPProvider(f'https://polygon-mainnet.infura.io/v3/{API_KEY_INFURA}'))
polygon_scan = ScanApi(rpc=pol, chain='MATIC', api_key=API_KEY_POLYGON_SCAN)
native_token_balance = polygon_scan.get_native_token_balance(account_address='0x3829cD969b481E32b77b32Bb7F41cD56BD95680A')
print(native_token_balance)