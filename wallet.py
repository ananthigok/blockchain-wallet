import os
from web3 import Web3
#from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account
from constants import *
import subprocess
import json
from pprint import pprint
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# enable PoA middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

def priv_key_to_account(coin, privkey):
    if (coin=="eth"):
        return Account.privateKeyToAccount(privkey)
    else:
        return PrivateKeyTestnet(privkey)

def create_raw_tx(account, recipient, amount, coin):
    if (coin=='eth'):
        value = w3.toWei(amount, "ether") # convert 1.2 ETH to 120000000000 wei
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": value}
        )
        return {
            "from": account.address,
            "to": recipient,
            "value": value,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    elif coin == 'btc':
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])


def send_tx(account, recipient, amount, coin):
    print ("**** COIN IS "+coin+" **** ")
    if coin == 'eth':
        tx = create_raw_tx(account, recipient, amount, coin)
        signed_tx = account.sign_transaction(tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        
    elif coin == 'btc':
        tx = create_raw_tx(account, recipient, amount, coin)
        signed_tx = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)    
    
## To Do put in env 
mnemonic = 'auto inside food rocket dignity service remember brand grit jacket iron goddess load athlete odor' #os.getenv("mnemonic")

def derive_wallets(coin=ETH, mnemonic=mnemonic, depth=3):
    cols= "all" #"path,address,index,privkey,pubkey,pubkeyhash"
    mnemonic = 'auto inside food rocket dignity service remember brand grit jacket iron goddess load athlete odor'
    print("coin is "+coin)
    cmd = f"php ./derive -g --mnemonic='{mnemonic}' --cols=path,address,privkey,pubkey --coin='{coin}' --numderive={depth} --format=json"
    print (cmd)
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True) #subprocess.run(cmd, shell=True, check=True)
    (data, err) = output.communicate()
    status = output.wait()
    data_formatted = json.loads(data)
    i=0
    for item in data_formatted:
        i += 1  
        ## 1,2,3 => eth
        ## 4,5,6 => btctest
        if (i==1):
            privkey = item.get('privkey')
            account = priv_key_to_account(coin, privkey)
        elif (i==2):
            recipient = item.get('address')
            amount = 0.01
            # prefund the account and then do the transaction 
            #create_raw_tx(account, recipient, amount, coin)
            #result = send_tx(account, recipient, amount, coin)
    return data_formatted

coins = {
    ETH: derive_wallets(coin=ETH),
    BTC: derive_wallets(coin=BTCTEST),
}
pprint(coins)
