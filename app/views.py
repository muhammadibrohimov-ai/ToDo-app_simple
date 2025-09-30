from django.shortcuts import render

from .models import ToDo

# Create your views here.

def all_todos(request):
    
    data = ToDo.objects.all()
    
    data = {
        data:'todo'
    }
    
    return render(request, "index.html",context=data)
