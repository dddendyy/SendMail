from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import home_view, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView, MessagesListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', home_view, name='homepage'),

    path('mailings/', MailingListView.as_view(), name='mailings_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('messages/', MessagesListView.as_view(), name='messages_list'),
    path('messages/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),

    path('clients/', ClientListView.as_view(), name='clients_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
