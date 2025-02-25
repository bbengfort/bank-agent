import json
import logging
import requests


# TODO: map users to authentication tokens in the database
TOKEN = "95fb9872d97faeca56ff999597bd39d27d3f751e"

logger = logging.getLogger("agent.tools")


def list_accounts(user: str) -> str:
    """
    Lists all of the accounts for the specified user.

    Args:
        user: The user whose accounts are to be listed.

    Returns:
        A JSON summary of account names and account numbers belonging to the user.
    """
    logger.info(f"listing accounts for user '{user}'")
    reply = requests.get(
        "http://localhost:8080/accounts/", headers={"Authorization": "Token " + TOKEN}
    )
    return json.dumps(reply.json())


def account_balance(account_number: str) -> str:
    """
    Gets the balance of the specified account.

    Args:
        account_number: The account number for the account to retreive the balance for.

    Returns:
        A JSON object with the account balance and other account details.
    """
    logger.info(f"account balance for account number '{account_number}'")

    if not account_number:
        return {"error": "No account number provided."}

    if account_number == "account_number":
        return {"error": "Must specify an account number."}

    reply = requests.get(
        f"http://localhost:8080/accounts/{account_number}/",
        headers={"Authorization": "Token " + TOKEN},
    )
    return json.dumps(reply.json())


def transfer_funds(credit: str, debit: str, amount: float) -> str:
    """
    Transfers funds from one account to another.

    Args:
        credit: The account number of the account to credit the funds from.
        debit: The account number of the account to debit the funds to.
        amount: The amount to transfer from the credit account to the debit account.

    Returns:
        A JSON object with the status of the transfer.
    """
    logger.info(
        f"transferring '{amount}' funds from credit account '{credit}' to debit account '{debit}'"
    )

    if not credit or not debit:
        return {"error": "Must specify credit and debit account numbers."}

    if not amount:
        return {"error": "Must specify an amount to transfer."}

    reply = requests.post(
        "http://localhost:8080/transfer/",
        headers={"Authorization": "Token " + TOKEN},
        json={"credit": credit, "debit": debit, "amount": amount},
    )
    return json.dumps(reply.json())
