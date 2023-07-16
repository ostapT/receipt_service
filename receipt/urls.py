from django.urls import path

from receipt.views import create_order

urlpatterns = [
    # Інші URL-маршрути вашого проекту
    path("create_order/", create_order, name="create_order"),
]

app_name = "receipt"
