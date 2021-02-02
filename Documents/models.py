from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(verbose_name="Название документ ", max_length=100)
    document = models.FileField(verbose_name="Файл", upload_to='document/', max_length=60)
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Документы"
        verbose_name_plural = "Документы"