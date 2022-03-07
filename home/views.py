from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('Hello World')


def students(request):
    context = {
        'all_students': [
            {
                'name': 'Alex',
                'is_olympic': True,
                'age': 20
            },
            {
                'name': 'Mircea',
                'is_olympic': False,
                'age': 21
            }
        ]
    }
    return render(request, 'home/all_students.html', context)


def brands(request):
    context = {
        'all_brands': [
            {
                'name': 'Mercedes',
                'model': 'CLS',
                'year': '2020'
            },
            {
                'name': 'Audi',
                'model': 'S7',
                'year': '2021'
            },
            {
                'name': 'Koenigsegg',
                'model': 'Agera RS',
                'year': '2014'
            }
        ]
    }
    return render(request, 'home/all_brands.html', context)


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'
