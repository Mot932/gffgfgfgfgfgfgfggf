from django.urls import path
from .views import index, index_1

urlpatterns = [
    path('index/', index),
    path('new_year/', index_1),
]