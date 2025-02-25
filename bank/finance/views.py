from rest_framework import viewsets
from finance.models import Account, Transfer
from finance.serializers import AccountsSerializer, TransferSerializer


class AccountsViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all().order_by("-created")
    serializer_class = AccountsSerializer


class TransactionsViewSet(viewsets.ModelViewSet):

    queryset = Transfer.objects.all().order_by("-executed")
    serializer_class = TransferSerializer
