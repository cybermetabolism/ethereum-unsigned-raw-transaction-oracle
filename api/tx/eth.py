###
# 
# /api/tx/raw_tx.py
#
# <Mercury> udtrokia@gmail.com
#
###

from web3.auto import w3;

class RawTxn:

    def __init__(self, _from, _to, _value):
        self.nonce = w3.eth.getTransactionCount(_from)
        self.gasprice = w3.eth.gasPrice
        self.startgas = w3.eth.getBlock("latest").gasLimit
        self.to = _to
        self.value = _value
        self.data = b'unframework'

    def to_dict(self):
        return self.__dict__;


# test
