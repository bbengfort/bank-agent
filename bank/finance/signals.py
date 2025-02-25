from .models import Transfer

from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(
    post_save,
    sender=Transfer,
    dispatch_uid="update_account_balance_after_transaction",
)
def update_balance_after_transaction(sender, instance, *args, **kwargs):
    # Subtract the amount from the credited account
    if instance.credit.account_type == "Credit":
        instance.credit.balance += instance.amount
    else:
        instance.credit.balance -= instance.amount
    instance.credit.save()

    # Add the amount to the debited account
    if instance.debit.account_type == "Credit":
        instance.debit.balance -= instance.amount
    else:
        instance.debit.balance += instance.amount
    instance.debit.save()
