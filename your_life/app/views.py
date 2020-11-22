from django.shortcuts import render
from django.views import View

# Create your views here.


class Index_view(View):
    def get(self, request):
        return render(request, 'app/index.html', context={})

class Calc_view(View):
    def get(self, request):
        return render(request, 'app/calculation.html', context={})

class Grath_view(View):
    def get(self, request):
        return render(request, 'app/grath.html', context={})

class Analysis_view(View):
    def get(self, request):
        return render(request, 'app/analysis.html', context={})