
from django.contrib import admin
from django.urls import path, include
from .views import Home, Users, Zones, Ips, Gui, DnsRecords

urlpatterns = [
    path('', Home.as_view()),
    path('gui/', Gui.as_view()),
    path('api/users/', Users.as_view()),
    path('api/zones/', Zones.as_view()),
    path('api/ips/', Ips.as_view()),
    path('api/dns_records/', DnsRecords.as_view()),
]
