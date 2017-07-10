from django.conf.urls import include, url
from . import views

from django.conf.urls import include, url
from packet_vis.views import api_v1_packets

urlpatterns = [
  url(r'^$', views.packet_list),
  # apiリクエストに対応
  url(r'^api/v1/packets$', api_v1_packets, name='api_v1_packets'),
]
