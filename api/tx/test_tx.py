# -*- coding: utf-8 -*-

###
#
#  api/tx/test_unsigned.py
#
#  <Mercury>: udtrokia@gmail.com
# 
###

import json;
import unsigned;

# EIP 155 chainId - mainnet: 1, ropsten: 3
tx_input = '{"nonce":"0x00","gasPrice":"0x09184e72a000","gasLimit":"0x2710","to":"0x0000000000000000000000000000000000000000","value":"0x00","data":"0x7f7465737432000000000000000000000000000000000000000000000000000000600057","chainId":3}'

tx_input_json = json.loads(tx_input);


def test(tx_json):
        unsigned_tx = unsigned.UnsignedTransaction(
            nonce = tx_json['nonce'],
            gasprice = tx_json['gasPrice'],
            startgas = tx_json['gasLimit'],
            to = tx_json['to'],
            value = tx_json['value'],
            data = tx_json['data']
        )
        print(unsigned_tx.to_dict());

test(tx_input_json);
