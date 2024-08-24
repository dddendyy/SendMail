from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField()
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return (f'{self.name}, {self.email}\n'
                f'{self.comment}')


class Message(models.Model):
    subject = models.CharField(max_length=300, verbose_name='тема')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return f'Письмо с темой {self.subject}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Attempt(models.Model):
    ATTEMPT_STATUS_CHOICE = [
        ('success', 'Удачно'),
        ('error', 'Ошибка')
    ]

    last_attempt_datetime = models.DateTimeField(verbose_name='дата/время последней попытки')
    status = models.CharField(max_length=15, choices=ATTEMPT_STATUS_CHOICE, verbose_name='статус')
    response = models.CharField(max_length=100, verbose_name='ответ почтового сервера')


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
    periodicity = models.CharField(max_length=30, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='статус')
    message = models.OneToOneField(Message, on_delete=models.SET_NULL, verbose_name='письмо', null=True, blank=True)
    client = models.ManyToManyField(Client, verbose_name='клиенты')
    attempts = models.ForeignKey(Attempt, on_delete=models.SET_NULL, verbose_name='попытки', null=True, blank=True)

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
