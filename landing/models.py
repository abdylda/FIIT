from django.db import models


# Create your models here.
class Category(models.Model):
    Naimenovanie = models.CharField("Категория", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Edizm(models.Model):
    Naimenovanie = models.CharField("ЕдИзм", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "ЕдИзм"
        verbose_name_plural = "ЕдИзм"


class NamKabinet(models.Model):
    Naimenovanie = models.CharField("Название кабинета", max_length=100)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Название кабинета"
        verbose_name_plural = "Название кабинета"


class Kabinet(models.Model):
    Naimenovanie = models.CharField("Кабинет", max_length=50)
    NamKabinet = models.ForeignKey(NamKabinet, verbose_name="Название кабинета", on_delete=models.CASCADE)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинет"


SOSTOYANIE = (
    ('рабочий', 'рабочий'),
    ('не рабочий', 'не рабочий')
)


class NalichiTehniki(models.Model):
    Kabinet = models.ForeignKey(Kabinet, verbose_name="Кабинет", on_delete=models.CASCADE)
    NamKabinet = models.ForeignKey(NamKabinet, verbose_name="Тип Кабинета", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    Edizm = models.ForeignKey(Edizm, verbose_name="Ед.изм.", on_delete=models.CASCADE, null=True)
    kodTMU = models.IntegerField(verbose_name="КодТМУ", default=11111111)
    Naimenovanie = models.CharField(max_length=255, verbose_name="Наименования", null=True)
    Kolich = models.IntegerField(verbose_name="Количество", default=1)
    sostoyanie = models.CharField(choices=SOSTOYANIE, verbose_name='Состояние', max_length=20, null=True)

    def _str_(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Наличие техники"
        verbose_name_plural = "Наличие техники"


class Engineer(models.Model):
    aty = models.CharField(verbose_name="ФИО", max_length=50)
    kabinet = models.ForeignKey(Kabinet, verbose_name="Кабинет", on_delete=models.CASCADE)
    doljnosti = models.CharField(verbose_name="Должность", max_length=100)
    tel = models.CharField(verbose_name="Номер телефона", max_length=30)
    start_work = models.CharField(verbose_name="время начала работы", max_length=10)
    end_work = models.CharField(verbose_name="время окончания работы", max_length=10)
    photo = models.ImageField(upload_to='engineer', null=True, )

    def __str__(self):
        return self.aty

    class Meta:
        verbose_name = "Инженеры и лаборанты"
        verbose_name_plural = "Инженеры и лаборанты"


class Ingener(models.Model):
    aty = models.CharField(verbose_name="ФИО", max_length=40)
    tel = models.CharField(verbose_name="Номер телефона", max_length=10)
    photo = models.ImageField(upload_to='фото', null=True, )

    def __str__(self):
        return self.aty

    class Meta:
        verbose_name = "Программист"
        verbose_name_plural = "Программист"


class Mebel(models.Model):
    aty = models.CharField(verbose_name="Аты", max_length=100)
    kabinet = models.ForeignKey(Kabinet, verbose_name="Кабинет", on_delete=models.CASCADE)
    engineer = models.ForeignKey(Engineer, verbose_name="Инженер", on_delete=models.CASCADE)
    Edizm = models.ForeignKey(Edizm, verbose_name="Ед.изм.", on_delete=models.CASCADE)
    kodTMU = models.IntegerField(verbose_name="КодТМУ")
    kolich = models.IntegerField(verbose_name="Количество")

    def __str__(self):
        return self.aty

    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"




