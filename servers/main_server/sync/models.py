from django.db import models
from django.contrib.auth.models import  User

# Create your models here.


class Empresa(models.Model):
    nombre = models.CharField(max_lengt=200)
    own = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Sync(models.Model):
    last_sync = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey()


