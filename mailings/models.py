from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField()
    comment = models.TextField(verbose_name='комментарий')


class Mailing(models.Model):

    PERIODICITY_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно')
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('launched', 'Запущена'),
        ('finished', 'Завершена')
    ]

    first_send_datetime = models.DateTimeField(verbose_name='дата/время первой отправки')
    periodicity = models.CharField(max_length=30, choices=PERIODICITY_CHOICES)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

