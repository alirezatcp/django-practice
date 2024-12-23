from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.DateField(blank=True, null=True)
    birth_date = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    public_date = models.DateField()
    pages_count = models.IntegerField()
    aauthor = models.ForeignKey(Author, on_delete=models.CASCADE)
