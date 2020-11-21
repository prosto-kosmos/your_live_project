from django.shortcuts import render
from django.views import View

# Create your views here.


class Start_view(View):
    def get(self, request):
        return render(request, 'app/start.html', context={})

class Main_view(View):
    def get(self, request):
        return render(request, 'app/main.html', context={})