from django.views import generic, View
from django.http import JsonResponse
from cloudflare.api import cf


class Home(generic.TemplateView):
    template_name = 'hqcf/home.html'

class Gui(generic.TemplateView):
    template_name = 'hqcf/gui.html'

class Zones(View):
    def get(self, request, **kwargs):
        return JsonResponse({'response': cf.get_zones()})

class Users(View):
    def get(self, request, **kwargs):
        return JsonResponse({'response': cf.get_users()})

class Ips(View):
    def get(self, request, **kwargs):
        return JsonResponse({'response': cf.get_ips()})

class Settings(View):
    def get(self, request, **kwargs):
        try:
            id = request.GET['id']
            return JsonResponse({'response': cf.get_settings(id)})
        except:
            return JsonResponse({})

class DnsRecords(View):
    def get(self, request, **kwargs):
        return JsonResponse({'response': cf.get_dns_records('5365db870036c405f700b50261707f25')})