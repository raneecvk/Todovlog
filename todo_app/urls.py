from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    # path('home',views.home,name='home'),
    path('',views.index,name='index'),
    path('taskview/',views.TaskListView.as_view(),name='taskview'),
    path('detailview/<int:pk>',views.TaskDetailView.as_view(),name='detailview'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')
]