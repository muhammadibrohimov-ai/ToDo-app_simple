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

def edit_todo(request, id):
    
    context = {
        'id':id
    }
    
    return render(request=request, template_name="edit.html", context=context)

def edit_todo_feature(request, id, num):
    
    context = {
        'id':id,
        'num': num
    }
    
    return render(request=request, template_name="edit_feature.html", context=context)


def full_edit(request, id, num):
    
    if request.POST:
        
        data = request.POST

        obj = ToDo.objects.get(id = id)
        
        if data.get('title'):
            title = data.get('title')
            obj.title = title

        
        if data.get('desc'): 
            desc = data.get('desc')
            obj.desc = desc
            
        
        if data.get('status'): 
            status = data.get('status')
            obj.status = status

        if data.get('date'): 
            date = data.get('date')
            time = data.get('time')
            date = datetime.strptime(date, "%Y-%m-%d")
            time = datetime.strptime(time, "%H:%M")

            date = date + timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
            
            obj.time = date

        obj.save()
        


    return redirect("/")