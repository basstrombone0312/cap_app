# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

import pymysql
from scapy.all import *
#from netaddr.ip import IPAddress

c = 0

connector = pymysql.connect(
  user='worker',
  passwd='packetworkerdata',
  host='',
  port='',
  db='packetdata',
  cursorclass=pymysql.cursors.DictCursor)

cursor = connector.cursor()

def packet_callback(packet):
  da = packet[0]['IP'].dst
  sa = packet[0]['IP'].src

  global c
  c=c+1

  sql = "INSERT INTO packet_vis_packet (d_addr, s_addr, d_port, s_port, time, iso_code) VALUES (%s, %s, %s, %s, %s, %s)"
  cursor.execute(sql, (sa, da, 1, 1, c, 'UNK'))
  connector.commit()

  if c == 1000:
    sql = "TRUNCATE TABLE packet_vis_packet"
    cursor.execute(sql,())
    connector.commit
    global c
    c = 0

sniff(prn=packet_callback, count=0)


