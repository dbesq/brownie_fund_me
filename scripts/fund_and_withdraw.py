from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account


def fund():
    print(f"FundMe length:  {len(FundMe)}")
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee, "gas_limit": 6721975})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
