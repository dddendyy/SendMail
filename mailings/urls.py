from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import home_view

app_name = MailingsConfig.name

urlpatterns = [
    path('', home_view, name='homepage')
]