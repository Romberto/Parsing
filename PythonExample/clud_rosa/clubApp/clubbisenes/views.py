from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from clubbisenes.models import Regions


def club_list(request, *args, **kwargs, ):
    contact = [
        'jack',
        'mike',
        'nicole '
    ]
    return render(request, 'clubbisenes/index.html', {'contacts': contact})


class Region(View):

    def get(self, request):
        regions = Regions.objects.all()
        return render(request, 'clubbisenes/region.html', {'regions': regions})


class Test(View):
    def get(self, request):
        return render(request, 'clubbisenes/test.html',{})