from django.db import models


class Messages(models.Model):
    text_message = models.TextField(verbose_name='Текст сообщения', name='text_message', max_length=400)
    pub_date = models.DateTimeField(verbose_name='Дата отправки', name='pub_date', auto_now_add=True)

    def __str__(self):
        return self.text_message

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
