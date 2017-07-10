from django.db import models

# Create your models here.
class Packet(models.Model):
  time = models.IntegerField()
  d_addr = models.BinaryField()
  s_addr = models.BinaryField()
  d_port = models.IntegerField()
  s_port = models.IntegerField()
  ip_prot = models.IntegerField()
  iso_code = models.CharField(max_length=16)

