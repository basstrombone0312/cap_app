from django.db import models

# Create your models here.
class Packet(models.Model):
  d_addr = models.CharField(max_length=64)
  s_addr = models.CharField(max_length=64)
  d_port = models.IntegerField()
  s_port = models.IntegerField()
  iso_code = models.CharField(max_length=16)
  time = models.IntegerField()
