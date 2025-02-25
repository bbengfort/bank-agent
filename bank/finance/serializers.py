from finance.models import Account, Transfer
from rest_framework import serializers


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ("url", "nickname", "account_number", "account_type")


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_number", "account_type", "nickname", "balance", "modified")


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ("memo", "credit", "debit", "amount", "executed")
