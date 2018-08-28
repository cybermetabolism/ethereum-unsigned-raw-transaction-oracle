## Transaction


#### 

#### TODO

+ data format?

+ nonce caulate?

+ chainId preview?

+ mock the front-end calling;



#### 

#### What is Transaction?

+ A transaction is stored as:  

  `[nonce, gasprice, startgas, to, value, data, v, r, s]`

+ nonce:  

  nonce is the number of transactions already sent by that account, encoded
  in binary form (eg.  0 -> '', 7 -> '\x07', 1000 -> '\x03\xd8').


+ v, r, s:  

  (v,r,s) is the raw Electrum-style signature of the transaction without the
  signature made with the private key corresponding to the sending account,
  with 0 <= v <= 3. From an Electrum-style signature (65 bytes) it is
  possible to extract the public key, and thereby the address, directly.


+ valid transaction:  

  (i) the signature is well-formed (ie. 0 <= v <= 3, 0 <= r < P, 0 <= s < N,
      0 <= r < P - N if v >= 2), and
  (ii) the sending account has enough funds to pay the fee and the value.

+ field
  
  + nonce:     big-endian-int
  + gasprice:  big-endian-int
  + startgas:  big-endian-int
  + to:        utils.address
  + value:     big-endian-int
  + data:      binary
  + v:         big-endian-int
  + r:         big-endian-int
  + s:         big-endian-int


#### 

#### Implement


+ Step 1

    convert website-input-data into the format data.


+ Step 2

    sign the format data to create a common transaction.
    

+ Step 3

    convert common transacion into raw transaction.


+ Step 4

    cook the API.


#### 

#### Test

```python
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
    print(c_txn.signed_txn.to_dict(), '\n')
    print(c_txn.raw_txn.as_dict());
    
test()

```



#### 

#### links

+ [pyethereum/.../transactions.py][1]
+ [eth-account/.../transactions.py][2]

[1]:https://github.com/ethereum/pyethereum/blob/develop/ethereum/transactions.py
[2]:https://github.com/ethereum/eth-account/blob/master/eth_account/internal/transactions.py
