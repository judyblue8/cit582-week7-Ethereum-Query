from web3 import Web3
from hexbytes import HexBytes
import math

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
#     print( "Connected to Ethereum node" )
    pass    
else:
    print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    t = w3.eth.get_transaction(tx)
    return t

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    gp = get_transaction(tx)['gasPrice']
    return gp

def get_gas(tx):
    gas = w3.eth.get_transaction_receipt(tx).gasUsed
    return gas

def get_transaction_cost(tx):
    cost = get_gas(tx) * get_gas_price(tx)
    return cost

def get_block_cost(block_num):
    block_cost = 1  # YOUR CODE HERE
    for t in w3.eth.get_block(block_num)['transactions']:
        block_cost += get_transaction_cost(t)
    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
    max_cost = 0
    for t in w3.eth.get_block(block_num)['transactions']:

        if get_transaction_cost(t) > max_cost:
            max_tx = t
            max_cost = get_transaction_cost(t)
    return max_tx


