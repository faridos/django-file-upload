# Create your models here.
from django.db import models


class ProfileImage(models.Model):
    image = models.BinaryField(editable = True)