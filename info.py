from ScanApi.scan_api import ScanApi
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from web3 import Web3
import os

load_dotenv(override=True)

API_KEY_INFURA = os.getenv('INFURA_API_KEY')


'''ARBITRUM'''
ARBITRUM_SCAN_API_KEY = os.getenv('ARBITRUM_SCAN_API_KEY')

arbitrum = Web3(Web3.HTTPProvider(f'https://arbitrum-mainnet.infura.io/v3/{API_KEY_INFURA}'))
arbitrum_scan = ScanApi(rpc=arbitrum, chain='ARBITRUM', api_key=ARBITRUM_SCAN_API_KEY)


'''BASE'''
MORALIS_NODE_BASE = os.getenv('MORALIS_NODE_BASE')
MORALIS_NODE_BASE2 = os.getenv('MORALIS_NODE_BASE2')
QUICK_NODE_BASE = os.getenv('QUICK_NODE_BASE_URL')
BASE_NODE_URL = os.getenv('BASE_NODE')
API_KEY_BASE_SCAN = os.getenv('BASE_SCAN_API_KEY')

base = Web3(Web3.HTTPProvider(QUICK_NODE_BASE))
# base = Web3(Web3.HTTPProvider(MORALIS_NODE_BASE))
# base = Web3(Web3.HTTPProvider(MORALIS_NODE_BASE2))
# base = Web3(Web3.HTTPProvider(BASE_NODE_URL))
base_scan = ScanApi(rpc=base, chain='BASE', api_key=API_KEY_BASE_SCAN)



'''BINANCE SMART CHAIN'''
API_KEY_BINANCE_SCAN = os.getenv('BINANCE_SCAN_API_KEY')
MORALIS_NODE_BSC = os.getenv('MORALIS_NODE_BSC')
QUICKNODE_BSC = os.getenv('QUICK_NODE_BSC_URL')

bsc = Web3(Web3.HTTPProvider(QUICKNODE_BSC))
# bsc = Web3(Web3.HTTPProvider(MORALIS_NODE_BSC))
bsc.middleware_onion.inject(geth_poa_middleware, layer=0)
bsc_scan = ScanApi(rpc=bsc, chain='bsc', api_key=API_KEY_BINANCE_SCAN)


'''POLYGON'''
API_KEY_POLYGON_SCAN = os.getenv('POLYGON_SCAN_API_KEY')

pol = Web3(Web3.HTTPProvider(f'https://polygon-mainnet.infura.io/v3/{API_KEY_INFURA}'))



'''ETHEREUM'''
ETHER_SCAN_API_KEY = os.getenv('ETHER_SCAN_API_KEY')

eth = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{API_KEY_INFURA}'))
ether_scan = ScanApi(rpc=eth, chain='ETH', api_key=ETHER_SCAN_API_KEY)


'''OPTIMISM'''
OPTIMISM_SCAN_API_KEY = os.getenv('OPTIMISM_SCAN_API_KEY')
op = Web3(Web3.HTTPProvider(f'https://optimism-mainnet.infura.io/v3/{API_KEY_INFURA}'))
optimism_scan = ScanApi(rpc=op, chain='OP', api_key=OPTIMISM_SCAN_API_KEY)
