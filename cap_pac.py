import pymysql
from scapy.all import *
import ipaddress
from netaddr.ip import IPAddress
import geoip2.database
import time

# GeoIP2データベースの読み込み
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

connector = pymysql.connect(
  user='worker',
  passwd='packetworkerdata',
  host='',
  port='', 
  db='packetdata',
  cursorclass=pymysql.cursors.DictCursor)

cursor = connector.cursor() 

c = 0
packet_list = []


def packet_callback(packet):
  global packet_list
  i=0
  try:
    ip = packet[0]['IP']    
  except:
    i = -1

  if i != -1:  
    #global packet_list
    #ip = packet[0]['IP']

    e = 0 
    try:
      record = reader.country(ip.src)
    # ローカルアドレスだったりデータベースに無かったりでエラーが出る
    except:
      e = -1

    if e == -1:
      code = 'UNK'
    elif e == 0:
      code = record.country.iso_code

    # UDP (proto number = 17)
    if ip.proto == 17:
      udp = ip['UDP']
      packet_list = packet_list + [{'da':ip.dst,
                                    'sa':ip.src,
                                    'ip_prot':17,
                                    'dp':udp.dport,
                                    'sp':udp.sport,
                                    'time':time.time(),
                                    'iso_code': code}]
    # TCP (proto number = 6)
    if ip.proto == 6:
      tcp = ip['TCP']
      packet_list = packet_list + [{'da':ip.dst,
                                    'sa':ip.src,
                                    'ip_prot':6,
                                    'dp':tcp.dport,
                                    'sp':tcp.sport,
                                    'time':time.time(),
                                    'iso_code': code}]  

    # 100件溜まったらDBにINSERT
    if len(packet_list) == 10:
      for item, _ in enumerate(packet_list):
        dic = packet_list[item] 
        sql = "INSERT INTO packet_vis_packet (d_addr, s_addr, d_port, s_port, ip_prot, time, iso_code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (format(int(IPAddress(dic['da'])),'b').zfill(32),
                             format(int(IPAddress(dic['sa'])),'b').zfill(32),
                             dic['dp'],
                             dic['sp'],
                             dic['ip_prot'],
                             dic['time'],
                             dic['iso_code']))
      # リストリセット
      packet_list = []
      # 100件一気にDBに本反映
      connector.commit()

      global c
      c += 1

  # 5000件溜まったらDBリセット
  #  if c == 50:
  #    sql = "TRUNCATE TABLE packet_vis_packet"
  #    cursor.execute(sql,())
  #    connector.commit
  #    c = 0


def main():
  sniff(prn=packet_callback, count=0, iface="enp0s3")


if __name__ == '__main__':
  main()
