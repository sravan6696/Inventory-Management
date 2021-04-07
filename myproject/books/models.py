from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=30, unique=True)
    name = models.TextField(max_length=1000)
    author = models.TextField(max_length=1000)
    count = models.IntegerField()

    def __str__(self):
        return self.name