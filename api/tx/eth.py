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


    def sign(self, priv_key):
        signed_txn = w3.eth.account.signTransaction(dict(
            nonce = self.nonce,
            gasPrice = self.gasprice,
            gas = self.startgas,
            to = self.to,
            value = self.value,
            data = self.data,
        ), priv_key);

        self.signed_txn = signed_txn;
        return signed_txn;

    def send(self):
        w3.eth.sendRawTransaction(self.signed_txn.rawTransaction)

# test
