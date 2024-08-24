from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from mailings.forms import MailingForm
from mailings.models import Mailing, Client


def home_view(request):
    """Возвращает домашнюю страницу"""
    return render(request, 'mailings/home.html')


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        client_list = self.object.client.all()
        context_data['client_list'] = client_list

        return context_data


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailings_list')
