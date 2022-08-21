from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index page'),
    path('view', views.view_emp, name='view_emp'),
    path('add', views.add_emp, name='add_emp'),
    path('remove', views.remove_emp, name='remove_emp'),
    path('remove/<int:id>', views.remove_emp, name='remove_emp'),
    path('filter', views.filter_emp, name='filter_emp'),
    path('filter/<int:id>', views.send_emp_to_edit, name='filter_emp'),
    path('edit', views.handle_emp, name="edit employee")
]
