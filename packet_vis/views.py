from django.shortcuts import render

from django.http import JsonResponse
from django.views import generic

from .models import Packet

import time


def packet_list(request):
  return render(request, 'packet_vis/packet_list.html', {})


def api_v1_packets(request):
  if request.method == 'GET':
    query = request.GET.get('query')
    tcp_packets = Packet.objects.filter(ip_prot = 6 , id__gt= query)
    udp_packets = Packet.objects.filter(ip_prot = 17 , id__gt= query) 

    max_id = len(Packet.objects.all())
    #last_packet = Packet.objects.filter(id = max_id).values()
    

    
    num_tcp = len(tcp_packets)
    num_udp = len(udp_packets)

    data = {
      'num_tcp':num_tcp,
      'num_udp':num_udp,
      'max_id': max_id,
      #'last_packet_time':last_packet[0]['time']
      'last_packet_time': time.time()
    }
    
    return JsonResponse(data)