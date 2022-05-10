import json
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'title': self.title,
            'substitle': self.subtitle,
            'author': self.author,
            'isbn': self.isbn
        }
