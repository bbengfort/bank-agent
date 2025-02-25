from django.db import models


class Account(models.Model):

    nickname = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    owners = models.ManyToManyField("auth.User", through="finance.Owner")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def last_four(self):
        return self.account_number[-4:]

    def __str__(self):
        return f"{self.nickname} (-{self.last_four})"


class Owner(models.Model):

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    account = models.ForeignKey("finance.Account", on_delete=models.CASCADE)
    permissions = models.CharField(max_length=2, choices=[("VO", "View Only"), ("IT", "Internal Transfers"), ("ET", "External Transfers")])

    def __str__(self):
        return f"{self.user.username} - {self.account.nickname}"


class Transfer(models.Model):

    memo = models.CharField(max_length=255)
    credit = models.ForeignKey(
        "finance.Account", related_name="transfers_credited", on_delete=models.CASCADE
    )
    debit = models.ForeignKey(
        "finance.Account", related_name="transfers_debited", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    executed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} from {self.debit.nickname} to {self.credit.nickname}"
