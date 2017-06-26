#!/home/fukushima/cap_app/venv/bin python3
# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

import pymysql
from packet_vis.models import Packet

 
from scapy.all import *
from netaddr.ip import IPAddress

def packet_callback(packet):
  da = int(IPAddress(packet[0]['IP'].dst))
  sa = int(IPAddress(packet[0]['IP'].src))

  p = Packet()
  p.d_port = 1
  p.s_port = 1
  time = 1
  p.d_addr = da
  p.s_addr = sa
  p.commit()


sniff(prn=packet_callback, count=0)



#c=0
#while True:
#    num = random.randint(1,100)

#    p = Packet()
#    p.number = num
#    p.created_date = timezone.now()
#    p.save()

#    time.sleep(1)
#    c = c+1

#    if c == 5:
#        pa = Post.objects.all()
#        pa.delete()
#        c=0
