from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import home_view, MailingListView, MailingDetailView

app_name = MailingsConfig.name

urlpatterns = [
    path('', home_view, name='homepage'),
    path('mailings/', MailingListView.as_view(), name='mailings_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail')
]