from django.shortcuts import render
from .models import Packet

# Create your views here.
def packet_list(request):
    return render(request, 'packet_vis/packet_list.html', {})
