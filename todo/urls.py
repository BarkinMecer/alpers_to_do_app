from django.urls import path
from . import views
app_name = 'todo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    path('addBranch/', views.addBranch, name='addBranch'),
    path('updateBranch/<str:branch_name>/', views.updateBranch, name='updateBranch'),
    path('deleteBranch/<str:branch_name>/', views.deleteBranch, name='deleteBranch'),
    path('branch/<int:pk>/', views.BranchDetail.as_view(), name='branch'),
   
    path('addfullToDo/', views.addFullToDo, name='addFullToDo'),
    path('addToDo/<str:branch_name>/', views.addToDo, name='addToDo'),
    path('updateToDo/<str:todo_title>/', views.updateToDo, name='updateToDo'),
    path('deleteToDo/<str:todo_title>/', views.deleteToDo, name='deleteToDo'),
    path('todoDetail/<int:pk>', views.ToDoDetailView.as_view(), name='todoDetail'),
    path('thanks/', views.thanks, name='thanks'),

    path('finishToDo/<int:todo_id>', views.finishToDo, name='finishToDo'),

    path('allToDos/', views.AllToDoView.as_view(), name='allToDos'),
    path('handledToDos/', views.HandledToDoView.as_view(), name='handledToDos'),
    path('soonComeToDos/', views.SoonComeToDoView.as_view(), name='soonComeToDos'),
]
