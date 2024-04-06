from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from django.conf import settings

from .models import Order
from .serializers import OrderSerializer

from pprint import pprint

from payme.methods.generate_link import GeneratePayLink


class CreateOrderView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        order = serializer.instance

        pay_link = GeneratePayLink(
            order_id=order.id,
            amount=serializer.data['amount'],
            callback_url=settings.PAYME['PAYME_CALL_BACK_URL']
        ).generate_link()

        data = {
            "link": pay_link,
            "order": serializer.data
        }

        return Response(status=status.HTTP_201_CREATED, data=data)
