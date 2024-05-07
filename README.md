## Prerequisites

:warning: 
You need to have [Python](https://python.org) installed on your machine

## How to run the application :arrow_forward:

### Git clone
In the terminal, clone the project: 

```
git clone https://github.com/Gb-dev371/ScanApi.git
```

### Virtual environment
Run the following command:
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Installing the requirements
```
pip install -r requirements.txt
```

### Adding environment variables
Next, set up your .env file with the necessary environment variables:

```bash
NODE_URL = 'your_base_node_url'
POLYGON_SCAN_API_KEY = ''
BINANCE_SCAN_API_KEY = ''
BASE_SCAN_API_KEY = ''
INFURA_API_KEY = ''
```

### Use case
## Getting a contract abi
```
from ScanApi.scan_api import ScanApi
base_scan = ScanApi(rpc=base, chain='BASE', api_key=API_KEY_BASE_SCAN)
contract_address = '0x16613524e02ad97eDfeF371bC883F2F5d6C480A5'
contract_abi = base_scan.get_contract_abi(contract_address)
```

## Getting an instancy of the contract
```
contract = base_scan.get_contract(contract_address, contract_abi)
```

## Getting the balance of the native token of an address in a specific chain
wallet_address = 'paste_a_valid_address_here'
native_balance = base_scan.get_native_token_balance(wallet_address)
print(native_balance)

### How to run the tests

```
Without test at the moment
```

### Tasks:

:memo: Add tests

:memo: Add more chains



### Developers/Contributors :octocat:

| [<img src="https://avatars.githubusercontent.com/u/116456573?v=4" width=115><br><sub>Gabriel Carvalho</sub>](https://github.com/Gb-dev371) 

### License

The [MIT License]() (MIT)

Copyright :copyright: 2024 - Hasselhoff