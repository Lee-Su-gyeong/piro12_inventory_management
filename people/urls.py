from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.people_list, name='people_list'),
    path('people/<int:pk>/', views.people_detail, name='people_detail'),
    path('people/create/', views.people_create, name='people_create'),
    path('people/update/<int:pk>/', views.people_update, name='people_update'),
    path('people/delete/<int:pk>/', views.people_delete, name="people_delete"),
]
