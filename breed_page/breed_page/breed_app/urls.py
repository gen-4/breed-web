from django.urls import path
from breed_page.breed_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('detailed/<id>', views.detailed, name='detailed_horse')
]