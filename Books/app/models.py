from django.db import models

class Book(models.Model):
    bookname = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.bookname
