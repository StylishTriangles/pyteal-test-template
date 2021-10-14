import os

import algosdk

MASTER_MNEMONIC = (
    "grape deer expand replace story mother audit ring universe lunar order dress metal"
    "term citizen replace recall april brick grunt erupt draw hole about harvest"
)

MASTER_PRIVATE_KEY = algosdk.mnemonic.to_private_key(MASTER_MNEMONIC)
MASTER_ADDRESS = "DW3FVR7PRSTUTOAUHJHQKX6ZKOZ5FGAHEBQMIMJA4SJYDX6452AZN7AOAE"

# token from devnet/primary/algod.token
ALGOD_TOKEN = "57f505e90015f61d91e8e9c6e0fa5fb0e391f1dce87af3e1fb21985fc616b7c3"
DEVNET_ADDRESS = os.getenv("DEVNET_ADDRESS", "http://127.0.0.1:8977")

client = algosdk.v2client.algod.AlgodClient(ALGOD_TOKEN, DEVNET_ADDRESS)
