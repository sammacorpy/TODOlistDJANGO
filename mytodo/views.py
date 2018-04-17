from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
# Create your views here.
from .models import *
from .forms import todoform

def homepage(request):
    tlist=todo.objects.order_by('id')
    total=todo.objects.count()
    tp=cmc=csus=0
    if total>0:
        cmc=todo.objects.filter(complete=1).count()/(total*1.0)*100
        csus=todo.objects.filter(suspended=1).count()/(total*1.0)*100
        tp=(total-cmc*total/100-csus*total/100)/total*100
    form=todoform()
    data={'title':'home','tlist':tlist,'form':form,'cmc':cmc,'csus':csus,'total':total,'tp':tp}
    return render(request,'mytodo/home.html',data)

@require_POST 
def addtask(request):
    form=todoform(request.POST)
    if form.is_valid():
        new=todo(title=request.POST['title'],desc=request.POST['desc'],lastdate=request.POST['lastdate'])
        new.save()
  
    return redirect('homepage')


@require_POST
def deletetask(request):
    tid=request.POST['id']
    todo.objects.filter(id=tid).delete()
    return redirect('homepage')


@require_POST
def completetask(request):
    tid=request.POST['id']
    obj=todo.objects.get(id=tid)
    obj.complete=True
    obj.suspended=False
    obj.save()
    return redirect('homepage')



@require_POST
def activatetask(request):
    tid=request.POST['id']
    obj=todo.objects.get(id=tid)
    obj.suspended=False
    obj.save()
    return redirect('homepage')



@require_POST
def suspendtask(request):
    tid=request.POST['id']
    obj=todo.objects.get(id=tid)
    obj.suspended=True
    obj.save()
    return redirect('homepage')


