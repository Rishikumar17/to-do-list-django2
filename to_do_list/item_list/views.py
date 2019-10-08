from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ItemList

# Create your views here.
def get_item_list_view(request):
    my_item_list = ItemList.objects.all()
    context = {
        'my_item':my_item_list
    }
    return render(request, 'base.html',context)

def addToDo(request):
    content = request.POST['activity']
    new_activity = ItemList(activity=content)
    new_activity.save()
    return HttpResponseRedirect('/')

def deleteItem(request,id):
    item_to_delete = ItemList.objects.get(id=id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
