from generator import OrphanTx;
from eth_account import Account;

def test():
    # acct = Account.create('unframework');
    # address = acct.address;
    # priv_key = acct.privateKey.hex();
    address = "0xBe71F82d69f8C6cbFA963B02d587c1310cb82cd6"
    priv_key = "0x6dcf391c697d8b691511ed3d2e3c1bc7f051cc8720b07e619f568d62e9f658c1"

    txn = {
        'nonce': 1024,
        'gasPrice': 2,
        'startgas': 3141592,
        'to': address,
        'value': 42,
        'data': b'This is Major Tom to Ground Control',
    }

    c_txn = OrphanTx(txn, priv_key);
    print("signed transaction: ");
    print(c_txn.signed_txn.to_dict(), '\n')

    print("raw transaction: ");
    print(c_txn.raw_txn.as_dict());
    
test()
