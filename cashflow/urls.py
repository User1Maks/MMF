from django.urls import path

from cashflow.apps import CashflowConfig
from cashflow.views import home

app_name = CashflowConfig.name

urlpatterns = [
    path("", home, name="home"),
]
