from typing import List


def list_accounts(user: str) -> List[str]:
    """
    Lists all of the accounts for the specified user.

    Args:
        user: The user whose accounts are to be listed.

    Returns:
        A list of account names.
    """
    return [
        "Four Start Checkings (-4031)",
        "Performance Savings (-1106)",
        "Cash Rewards Visa (-7931)",
    ]


def account_balance(account: str) -> float:
    """
    Gets the balance of the specified account.

    Args:
        account: The account whose balance is to be retrieved.

    Returns:
        The account balance.
    """
    return 1234.56


def transfer_funds(credit: str, debit: str, amount: float) -> bool:
    """
    Transfers funds from one account to another.

    Args:
        credit: The account to credit.
        debit: The account to debit.
        amount: The amount to transfer.

    Returns:
        True if the transfer was successful, False otherwise.
    """
    return True
