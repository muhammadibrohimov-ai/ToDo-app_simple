from django.shortcuts import render, redirect

from .models import ToDo

from datetime import datetime, timedelta
# Create your views here.

def all_todos(request):
    
    data = ToDo.objects.all()
    
    data = {
        'todo':data
    }
    
    return render(request = request, template_name = "index.html",context=data)


def create_todo(request):
    
    if request.POST:
        data = request.POST

        title = data.get('title')
        desc = data.get('desc')
        date = data.get('date')
        time = data.get('time')
        status = data.get('status')

        date = datetime.strptime(date, "%Y-%m-%d")
        time = datetime.strptime(time, "%H:%M")

        date = date + timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

        ToDo.objects.create(
            title = title,
            desc=desc,
            time=date,
            status=status
        )


    return redirect("/")

def delete_todo(request, id):
    data = ToDo.objects.get(id = id)
    if data:
        data.delete()
        
    
    return redirect("/")
