pragma solidity ^0.4.20;
//a loaded 'state'. The state is unaware of it's surrounding world -
//it doesnt know if the transaction is valid or not. 
contract tokenState {
    /* This creates an array with all balances */
    bytes8 displacement;
    bytes32 signature;
    address from;
    address to;
    bool spent;

    //load a given 'state' 
    function tokenState(bytes input, bytes signature) public {
        processState(input);
        
        //verify address from input is signed in the signature
        require(smartVerf.ecverify(sha3(input), signature, from));
    }
    
    /*Break up a given 'bytes' input into seperate values, 
    Such as to, from, and amount displaced.
    ex:
    
    input: "0x8215292337Ce0b5cbfFeFa7292B7C8224f15b241a0843d40f1cdad7a0ad7826abcc309d90561512c42"
    gets broken down into    

    to: 8215292337Ce0b5cbfFeFa7292B7C8224f15b241
    from: a0843d40f1cdad7a0ad7826abcc309d90561512c
    displacement: 000000000000000042"

    Current "displacement" comes in the form of a bytes8, allowing a uint256 is
    on to do list
    */
    function processState(bytes input) public {
        address to_adder_assembly;
        address from_adder_assembly;
        bytes8 displacement_assembly;
        
        assembly {
            to_adder_assembly := mload(add(input, 20))
            from_adder_assembly := mload(add(input, 40))
            displacement_assembly := mload(add(input, 73))
        }
        
        to = to_adder_assembly;
        from = from_adder_assembly;
        displacement = displacement_assembly;
    }
    
    
}


//credit to https://gist.github.com/axic
library smartVerf{
    function safer_ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) internal returns (bool, address) {
        // We do our own memory management here. Solidity uses memory offset
        // 0x40 to store the current end of memory. We write past it (as
        // writes are memory extensions), but don't update the offset so
        // Solidity will reuse it. The memory used here is only needed for
        // this context.

        // FIXME: inline assembly can't access return values
        bool ret;
        address addr;

        assembly {
            let size := mload(0x40)
            mstore(size, hash)
            mstore(add(size, 32), v)
            mstore(add(size, 64), r)
            mstore(add(size, 96), s)

            // NOTE: we can reuse the request memory because we deal with
            //       the return code
            ret := call(3000, 1, 0, size, 128, size, 32)
            addr := mload(size)
        }

        return (ret, addr);
    }

    function ecrecovery(bytes32 hash, bytes sig) returns (bool, address) {
        bytes32 r;
        bytes32 s;
        uint8 v;

        if (sig.length != 65)
          return (false, 0);

        // The signature format is a compact form of:
        //   {bytes32 r}{bytes32 s}{uint8 v}
        // Compact means, uint8 is not padded to 32 bytes.
        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))

            // Here we are loading the last 32 bytes. We exploit the fact that
            // 'mload' will pad with zeroes if we overread.
            // There is no 'mload8' to do this, but that would be nicer.
            v := byte(0, mload(add(sig, 96)))

            // Alternative solution:
            // 'byte' is not working due to the Solidity parser, so lets
            // use the second best option, 'and'
            // v := and(mload(add(sig, 65)), 255)
        }

        if (v < 27)
          v += 27;

        if (v != 27 && v != 28)
            return (false, 0);

        return safer_ecrecover(hash, v, r, s);
    }

    function ecverify(bytes32 hash, bytes sig, address signer) returns (bool) {
        bool ret;
        address addr;
        (ret, addr) = ecrecovery(hash, sig);
        return ret == true && addr == signer;
    }
}
