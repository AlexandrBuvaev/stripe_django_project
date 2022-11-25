from django.db import models


class Item(models.Model):
    """
    Модель для хранения вещи
    в базе данных.
    """
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', max_length=300)
    price = models.IntegerField('Цена', default=0)

    def __str__(self):
        return self.name
