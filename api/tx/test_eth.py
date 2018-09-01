##
#
# /tx/api/test_eth.py
#
# <Mercury> udtrokia@gmail.com
# 
##

import eth;

priv_key = "0x6dcf391c697d8b691511ed3d2e3c1bc7f051cc8720b07e619f568d62e9f658c1"
ADDRESS = "0xBe71F82d69f8C6cbFA963B02d587c1310cb82cd6"

def test_RawTxn():
    raw_txn = eth.RawTxn(ADDRESS, ADDRESS, 42);
    signed_txn = raw_txn.sign(priv_key);
    
    print("rawtxn:  ", raw_txn.to_dict());
    print("signedtxn:  ", signed_txn);


## test ##
test_RawTxn();
