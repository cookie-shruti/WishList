
from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=133)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Services(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

def __str__(self):
    return self.title + ' | ' + str(self.author)


def get_absolute_url(self):
    return reverse('detail', args=(str(self.id)))
    