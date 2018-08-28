##
#
# /tx/api/test_eth.py
#
# <Mercury> udtrokia@gmail.com
# 
##

import eth;

ADDRESS = "0xBe71F82d69f8C6cbFA963B02d587c1310cb82cd6"

def test_RawTxn():
    raw_txn = eth.RawTxn(ADDRESS, ADDRESS, 42);
    print('\n--- raw_txn ---');
    print(raw_txn.to_dict());
    print('---------------\n');



## test ##
test_RawTxn();
