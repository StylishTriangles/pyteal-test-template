from copy import copy
import time

import algosdk
from algosdk.future.transaction import SuggestedParams, PaymentTxn, AssetOptInTxn, ApplicationOptInTxn

from tests.constants import client, MASTER_ADDRESS, MASTER_PRIVATE_KEY


class Account:
    """
    An account on the blockchain
    """
    def __init__(self, private_key: str = None, addr: str = None):
        if addr is None:
            addr = algosdk.account.address_from_private_key(private_key)

        self.private_key = private_key
        self.address = addr

def sp_zero_fee(sp: SuggestedParams) -> SuggestedParams:
    """
    Copy suggested params and use 0 fees
    """
    sp = copy(sp)
    sp.flat_fee = True
    sp.fee = 0
    return sp

def sp_large_fee(sp: SuggestedParams) -> SuggestedParams:
    """
    Copy suggested params and return suggested params with fee that could pay for 16 txns
    """
    sp = copy(sp)
    sp.flat_fee = True
    sp.fee = 16000
    return sp

def now() -> int:
    """
    Curent UNIX timestamp
    """
    return int(time.time())

def suggested_params() -> SuggestedParams:
    """
    Can be changed to add caching for example
    """
    return client.suggested_params()

def create_account(initial_microalgos: int = 10000000, assets: list = None, apps: list = None) -> Account:
    """
    Create a new account, send some algos to it and opt it in to assets and apps
    """
    if assets is None:
        assets = []
    if apps is None:
        apps = []

    pk, addr = algosdk.account.generate_account()
    acc = Account(pk, addr)
    sp = suggested_params()

    client.send_transaction(
        PaymentTxn(MASTER_ADDRESS, sp, acc.address, initial_microalgos).sign(MASTER_PRIVATE_KEY)
    )

    for asset in assets:
        client.send_transaction(
            AssetOptInTxn(MASTER_ADDRESS, sp, asset).sign(pk)
        )

    for app in apps:
        client.send_transaction(
            ApplicationOptInTxn(MASTER_ADDRESS, suggested_params(), app).sign(pk)
        )

    return acc