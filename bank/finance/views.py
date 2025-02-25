from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from finance.models import Account, Transfer
from django.shortcuts import get_object_or_404
from finance.serializers import AccountsSerializer, BalanceSerializer, TransferSerializer


class AccountsViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all().order_by("-created")
    lookup_field = "account_number"
    serializer_class = AccountsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(owners=self.request.user)

    def retrieve(self, request, account_number=None):
        queryset = self.get_queryset().filter(owners=request.user)
        account = get_object_or_404(queryset, account_number=account_number)
        serializer = BalanceSerializer(account, context={"request": request})
        return Response(serializer.data)


class TransferViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Transfer.objects.all().order_by("-executed")
    serializer_class = TransferSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            Q(debit__owners=self.request.user) | Q(credit__owners=self.request.user)
        )
