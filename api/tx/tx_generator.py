# -*- coding: utf-8 -*-

###
#
#  /api/tx/tx_generator.py
# 
#  <Mercury> udtrokia@gmail.com
#
##  TODO: 
#  
#  1. convert website-input-data into transactions
#
#  2. sign the format data into common transaction
#
##


# test data;
data = {
    "data": "unframework"
    "from": "0xbb5c52d9ab611fca798ddae930c7fc8307efdc11",    
    "gasPrice": 6,
    "gasLimit": 25000,
    "to": "0x8d12a197cb00d4747a1fe03395095ce2a5cc6819",    
    "value": "0.02",
}

class OrphanTx:
    fields = [
        ('gasPrice', int),
        ('gasLimit', int),
        ('to', str),
        ('value', float),
        ('data', str),
    ]

    """output

    fields = [
        ('nonce', big_endian_int),
        ('gasprice', big_endian_int),
        ('startgas', big_endian_int),
        ('to', utils.address),
        ('value', big_endian_int),
        ('data', binary),
        ('v', big_endian_int),
        ('r', big_endian_int),
        ('s', big_endian_int),
    ]    

    """
    self.nonce = None;
    self.gasPrice = None;
    self.gasLimit = None;
    self.to = None;
    self.value = None;
    self.data = None;
    self.v = None;
    self.r = None;
    self.s = None;
    
    def __init__(self):

        # ...reset self fields format;

        
    def sign(self):

        # ...sign and return a new Tx;
    

def test():
    # ...test
