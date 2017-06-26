#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import sys
#sys.path.append('~/cap_app')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foo")
import django
django.setup()


from packet_vis.models import Packets

 
from scapy.all import *

def packet_callback(packet):
  p = Packet()
  p.d_addr = packet[0]['IP'].dst
  p.s_addr = packet[0]['IP'].src
  p.save()

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
