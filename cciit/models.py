from datetime import timezone

from django.db import models


# Create your models here.

class Unit(models.Model):
    Name = models.CharField("ЕдИзм", max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "ЕдИзм"
        verbose_name_plural = "ЕдИзм"


class Categories(models.Model):
    Name = models.CharField("Категория", max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Cabinet_name(models.Model):
    Name = models.CharField("Название кабинета", max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Название кабинета"
        verbose_name_plural = "Название кабинета"


class Cabinet(models.Model):
    Name = models.CharField("Кабинет", max_length=50)
    Cabinet_name = models.ForeignKey(Cabinet_name, verbose_name="Название кабинета", on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинет"


class Engineers(models.Model):
    fio = models.CharField(verbose_name="ФИО", max_length=50)
    Cabinet = models.ForeignKey(Cabinet, verbose_name="Кабинет", on_delete=models.SET_NULL, null=True)
    position = models.CharField(verbose_name="Должность", max_length=100)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=30)
    start_work = models.CharField(verbose_name="время начала работы", max_length=10)
    end_work = models.CharField(verbose_name="время окончания работы", max_length=10)
    photo = models.ImageField(upload_to='engineer', null=True, )
    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Инженеры"
        verbose_name_plural = "Инженеры"


SOSTOYANI = (
    ('рабочий', 'рабочий'),
    ('не рабочий', 'не рабочий')
)


class Available_techniques(models.Model):
    Cabinet = models.ForeignKey(Cabinet, verbose_name="Кабинет", on_delete=models.CASCADE)
    Cabinet_name = models.ForeignKey(Cabinet_name, verbose_name="Тип Кабинета", on_delete=models.CASCADE)
    Categories = models.ForeignKey(Categories, verbose_name="Категории", on_delete=models.CASCADE)
    Unit = models.ForeignKey(Unit, verbose_name="Ед.изм.", on_delete=models.CASCADE, null=True)
    KODTMU = models.IntegerField(verbose_name="КодТМУ", default=11111111)
    Names = models.CharField(max_length=255, verbose_name="Наименования", null=True)
    Quantity = models.IntegerField(verbose_name="Количество", default=1)
    sostoyani = models.CharField(choices=SOSTOYANI, verbose_name='Состояние', max_length=20, null=True)

    def _str_(self):
        return self.Names

    class Meta:
        verbose_name = "Наличие техники"
        verbose_name_plural = "Наличие техники"


