from finance.models import Account, Transfer
from rest_framework import serializers


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ("url", "nickname", "account_number", "account_type")
        lookup_field = "account_number"
        extra_kwargs = {
            "url": {"lookup_field": "account_number"}
        }


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_number", "account_type", "nickname", "balance", "modified")


class TransferSerializer(serializers.ModelSerializer):

    credit = serializers.SlugRelatedField(slug_field="account_number", queryset=Account.objects.all())
    debit = serializers.SlugRelatedField(slug_field="account_number", queryset=Account.objects.all())

    class Meta:
        model = Transfer
        fields = ("memo", "credit", "debit", "amount", "executed")
