from brownie import FundMe, MockV3Aggregator, accounts, network, config

local_developmet_env = ["development", "ganache-local"]


def get_account():
    print(network.show_active())
    if network.show_active() in local_developmet_env:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
