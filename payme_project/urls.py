
from django.contrib import admin
from django.urls import path

from main.payments import PaymeCallBackAPIView
from main.views import CreateOrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("payments/merchant/", PaymeCallBackAPIView.as_view()),
    path("payments/create-order/", CreateOrderView.as_view()),
]
