from django.db import models


# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=120 , verbose_name='Basliq')
    content = models.TextField(verbose_name='Icerik')
    publishing_date = models.DateTimeField(verbose_name='yayin tarixi')

    def __str__(self):
        return self.publishing_date