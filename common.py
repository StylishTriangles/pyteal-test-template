"""
Common useful operations for interacting with the ledger state
"""
from base64 import b64decode
from typing import Optional
from algosdk.v2client.algod import AlgodClient

def process_key_value(kv: list) -> dict[str, str or int]:
    """
    Transform Algorand key-value schema into python dict with key value pairs
    """
    res = {}
    for elem in kv:
        key = str(b64decode(elem["key"]), encoding="ascii")
        if elem["value"]["type"] == 1:
            val = elem["value"]["bytes"]  # type: str
        else:
            val = elem["value"]["uint"]  # type: int
        res[key] = val
    return res

def get_local_state(client: AlgodClient, address: str, app_id: int) -> Optional[dict[str, str or int]]:
    """
    Get the local state of an account for a given app

    Args:
        client: Algod client
        address: address of the account to check
        app_id: Algorand application ID of an app to use

    Returns:
        None when the account is not opted in to app, dict of key-values of the local state
    """
    info = client.account_info(address)
    apps_local_state = info["apps-local-state"]  # type: list
    try:
        app_local_state = next(filter(lambda el: el["id"] == app_id, apps_local_state))
    except StopIteration:
        return None
    return process_key_value(app_local_state["key-value"])

def get_global_state(client: AlgodClient, app_id: int) -> dict[str, str or int]:
    """
    Get the global state of the application
    """
    info = client.application_info(app_id)
    app_global_state = info["params"]["global-state"]
    return process_key_value(app_global_state)

def get_assets(client: AlgodClient, address: str) -> dict[int, int]:
    """
    Get amounts of owned assets by a given address

    Returns:
        dict mapping asset ids to asset holdings
    """
    info = client.account_info(address)
    assets = info["assets"]  # type: list

    return {
        asset["asset-id"]: asset["amount"]
        for asset
        in assets
    }
