from django.shortcuts import render
from django.views.generic import ListView

from mailings.models import Mailing


def home_view(request):
    """Возвращает домашнюю страницу"""
    return render(request, 'mailings/home.html')


class MailingListView(ListView):
    model = Mailing
