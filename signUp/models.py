from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SignUp(models.Model):
    username = models.CharField(max_length=254)
    email = models.EmailField()
    date = models.DateTimeField(verbose_name="Date inscription", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.username + "->" + self.email
