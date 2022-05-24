from django.shortcuts import render
from django.http import HttpResponse

# Это контроллер и MVC

def index(request):
    print(request)
    return HttpResponse('Мы пришли к этому в конце 3-ей пары! Ура! Ура! Ура!')
def test(request):
    print(request)
    return HttpResponse('<H1> TEST </H1>')