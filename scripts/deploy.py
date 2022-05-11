from brownie import FundMe, MockV3Aggregator, accounts, network, config

local_developmet_env = ["development", "ganache-local"]


def deploy_fund_me():
    account = get_account()
    print(account)
    if network.show_active() not in local_developmet_env:
        price_feed_address = "0x9326BFA02ADD2366b30bacB125260Af641031331"
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    print(f"Contract depolyed to {fund_me.address}")

    return fund_me


def get_account():
    print(network.show_active())
    if network.show_active() in local_developmet_env:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    print(len(MockV3Aggregator))
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(
            18, 200000000000000000, {"from": get_account()}
        )
        print("Mocks Deployed!")


def main():
    deploy_fund_me()
