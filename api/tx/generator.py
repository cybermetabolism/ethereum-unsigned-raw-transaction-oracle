# -*- coding: utf-8 -*-

###
#
#  /api/tx/generator.py
# 
#  <Mercury> udtrokia@gmail.com
#
##  TODO: Mock the data deliver from the web-form

import pyeth_tx;
from eth_utils.curried import (from_wei, to_wei);

class OrphanTx:

    def __init__(self, txn, priv_key):

        signed_txn = pyeth_tx.Transaction(
            nonce = txn['nonce'],
            gasprice = txn['gasPrice'],
            startgas = txn['startgas'],
            to = txn['to'],
            value = txn['value'],
            data = txn['data'],
        ).sign(priv_key);

        raw_txn = pyeth_tx.unsigned_tx_from_tx(signed_txn);
        # raw_txn['to'] = '0x'+ raw_txn['to'].hex();

        self.signed_txn = signed_txn;
        self.raw_txn = raw_txn;
        



