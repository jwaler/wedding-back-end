from django.db import models

# Create your models here.
class Guest(models.Model):
    nom = models.CharField(max_length=250, blank=False, null=False)
    email = models.CharField(max_length=250, blank=False, null=False)
    attend = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.nom