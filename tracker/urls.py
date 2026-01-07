from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),   # Homepage shows list
    path('add/', views.add_expense, name='add_expense'), # Add form
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
]
