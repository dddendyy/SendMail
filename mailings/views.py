from django.shortcuts import render


def home_view(request):
    """Возвращает домашнюю страницу"""
    return render(request, 'mailings/home.html')
