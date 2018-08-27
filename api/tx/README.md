## Transaction

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
