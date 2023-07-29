from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addContent/', views.addContent, name='addContent'),
    path('updateContent/', views.updateContent, name='updateContent')
]
