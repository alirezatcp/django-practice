from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    public_date = models.DateField()
    pages_count = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    hidden = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('hide_book', 'Can make book hidden') # (codename, name)
        ]

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100)


# custom User model.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) # rewrite email and add unique=True
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    # now we should add CustomUser to settings: AUTH_USER_MODEL = 'app_name.User_model_name'