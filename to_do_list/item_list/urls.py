from django.urls import path
from .views import get_item_list_view, addToDo, deleteItem
urlpatterns = [
    path('',get_item_list_view,name='item-list-view'),
    path('deleteItem/<int:id>/',deleteItem,name='deleteItem'),
    path('addToDo/',addToDo,name='addToDo'),
]
